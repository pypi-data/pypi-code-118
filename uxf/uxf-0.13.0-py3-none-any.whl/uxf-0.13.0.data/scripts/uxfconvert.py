#!python
# Copyright © 2022 Mark Summerfield. All rights reserved.
# License: GPLv3

import argparse
import configparser
import csv
import datetime
import json
import pathlib
import shutil
import sqlite3
import sys
import textwrap

import uxf


def main():
    config = _get_config()
    try:
        config.convert(config)
    except (FileNotFoundError, uxf.Error) as err:
        print(err, file=sys.stderr)


def _get_config():
    parser = argparse.ArgumentParser(usage=PREFIX + _get_usage())
    parser.add_argument('-i', '--indent', type=int, default=2,
                        help='default: 2, range 0-8')
    parser.add_argument(
        '-f', '--fieldnames', action='store_true',
        help='if set the first row of csv file(s) is read as field names; '
        'default: all rows are values')
    parser.add_argument('file', nargs='+',
                        help='infile(s) and outfile as shown above')
    config = parser.parse_args()
    _postprocess_args(parser, config)
    return config


def _get_usage():
    try:
        term_width = shutil.get_terminal_size()[0]
    except AttributeError:
        term_width = 80
    return '\n\n'.join('\n'.join(textwrap.wrap(para.strip(), term_width))
                       for para in USAGE.strip().split('\n\n')
                       if para.strip())


def _postprocess_args(parser, config):
    if not (0 <= config.indent <= 8):
        config.indent = 2 # sanitize rather than complain
    if len(config.file) < 2:
        parser.error('least two filenames are required')
    config.convert = None
    if len(config.file) > 2:
        _postprocess_csv_args(parser, config)
    else:
        _postprocess_other_args(parser, config)
    if config.convert is None:
        parser.error('cannot perform the requested conversion')
    del config.file
    return config


def _postprocess_csv_args(parser, config):
    if not config.file[-1].upper().endswith((DOT_UXF, DOT_UXF_GZ)):
        parser.error('multiple infiles may only be converted to .uxf')
    for name in config.file[:-1]:
        if not name.upper().endswith(DOT_CSV):
            parser.error('multiple infiles may only be .csv files')
    config.convert = multi_csv_to_uxf
    config.infiles = config.file[:-1]
    config.outfile = config.file[-1]


def _postprocess_other_args(parser, config):
    config.infiles = [config.file[0]]
    config.outfile = config.file[-1]
    infile = config.infiles[0].upper()
    outfile = config.outfile.upper()
    if (infile.endswith((DOT_UXF, DOT_UXF_GZ)) and
            outfile.endswith((DOT_UXF, DOT_UXF_GZ))):
        parser.error('connot convert uxf to uxf, instead use: '
                     'python3 -m uxf infile.uxf outfile.uxf')
    if outfile.endswith((DOT_UXF, DOT_UXF_GZ)):
        if infile.endswith(DOT_CSV):
            config.convert = csv_to_uxf
        elif infile.endswith(DOT_INI):
            config.convert = ini_to_uxf
        elif infile.endswith((DOT_JSN, DOT_JSON)):
            config.convert = json_to_uxf
        elif infile.endswith(DOT_SQLITE):
            config.convert = sqlite_to_uxf
        elif infile.endswith(DOT_XML):
            config.convert = xml_to_uxf
    elif infile.endswith((DOT_UXF, DOT_UXF_GZ)):
        if outfile.endswith(DOT_CSV):
            config.convert = uxf_to_csv
        elif outfile.endswith((DOT_JSN, DOT_JSON)):
            config.convert = uxf_to_json
        elif outfile.endswith(DOT_SQLITE):
            config.convert = uxf_to_sqlite
        elif outfile.endswith(DOT_XML):
            config.convert = uxf_to_xml


def uxf_to_csv(config):
    uxf_obj = uxf.load(config.infiles[0])
    data = uxf_obj.data
    if isinstance(data, uxf.Table):
        with open(config.outfile, 'w') as file:
            writer = csv.writer(file, quoting=csv.QUOTE_NONNUMERIC)
            writer.writerow((field.name for field in data.fields))
            for row in data:
                writer.writerow(row)
    elif (isinstance(data, (list, uxf.List)) and data and
            isinstance(data[0], (list, uxf.List)) and data[0] and not
            isinstance(data[0][0], (dict, list, uxf.Map, uxf.List,
                                    uxf.Table))):
        with open(config.outfile, 'w') as file:
            writer = csv.writer(file, quoting=csv.QUOTE_NONNUMERIC)
            for row in data:
                writer.writerow(row)
    else:
        raise SystemExit('can only convert a UXF containing a single table '
                         'or a single list of lists of scalars to csv')


def csv_to_uxf(config):
    data, filename, ttypes = _read_csv_to_data(config)
    uxf.dump(config.outfile, uxf.Uxf(data, filename, ttypes=ttypes),
             one_way_conversion=True)


def _read_csv_to_data(config):
    ttypes = {}
    data = None
    filename = config.infiles[0]
    with open(filename) as file:
        reader = csv.reader(file)
        for row in reader:
            if data is None:
                if config.fieldnames:
                    name = uxf.canonicalize(pathlib.Path(filename).stem)
                    data = uxf.Table(name=name, fields=[uxf.Field(name)
                                     for name in row])
                    ttypes[name] = data.ttype
                    continue
                else:
                    data = []
            row = [uxf.naturalize(x) for x in row]
            if isinstance(data, uxf.Table):
                data += row
            else:
                data.append(row)
    return data, filename, ttypes


def multi_csv_to_uxf(config):
    infiles = config.infiles
    data = []
    ttypes = {}
    for infile in infiles:
        config.infiles = [infile]
        datum, _, new_ttypes = _read_csv_to_data(config)
        data.append(datum)
        if new_ttypes:
            ttypes.update(new_ttypes)
    uxf.dump(config.outfile,
             uxf.Uxf(data, ' '.join(infiles), ttypes=ttypes),
             one_way_conversion=True)


def uxf_to_json(config):
    uxf_obj = uxf.load(config.infiles[0])
    data = {JSON_CUSTOM: uxf_obj.custom,
            JSON_TTYPES: list(uxf_obj.ttypes.values()),
            JSON_DATA: uxf_obj.data}
    with open(config.outfile, 'wt', encoding=UTF8) as file:
        json.dump(data, file, cls=_JsonEncoder, indent=2)


class _JsonEncoder(json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return {JSON_DATETIME: obj.isoformat()}
        if isinstance(obj, datetime.date):
            return {JSON_DATE: obj.isoformat()}
        if isinstance(obj, (bytes, bytearray)):
            return {JSON_BYTES: obj.hex().upper()}
        if isinstance(obj, (list, uxf.List)):
            comment = getattr(obj, COMMENT, None)
            vtype = getattr(obj, VTYPE, None)
            if comment is None and vtype is None:
                return list(obj)
            return {JSON_LIST: dict(comment=comment, vtype=vtype,
                                    list=list(obj))}
        if isinstance(obj, uxf.Map):
            return _json_encode_map(obj)
        if isinstance(obj, dict):
            return obj
        if isinstance(obj, uxf.Table):
            return {JSON_TABLE: dict(
                name=obj.name, comment=obj.comment,
                fields={field.name: field.vtype for field in obj.fields},
                records=obj.records)}
        if isinstance(obj, uxf.TType):
            return {JSON_TTYPE: dict(
                name=obj.name,
                fields={field.name: field.vtype for field in obj.fields})}
        return json.JSONEncoder.default(self, obj)


def _json_encode_map(obj):
    comment = getattr(obj, COMMENT, None)
    ktype = getattr(obj, KTYPE, None)
    vtype = getattr(obj, VTYPE, None)
    d = {}
    itypes = {}
    for key, value in obj.items():
        if isinstance(key, (datetime.date, datetime.datetime)):
            skey = key.isoformat()
            itypes[skey] = UXF
        elif isinstance(key, int):
            skey = str(key)
            itypes[skey] = UXF
        elif isinstance(key, (bytes, bytearray)):
            skey = key.hex().upper()
            itypes[skey] = BYTES
        elif isinstance(key, str):
            skey = key
        else:
            raise SystemExit(f'invalid map key type: {key} of {type(key)}')
        d[skey] = value
    if not itypes and comment is None and ktype is None:
        return dict(obj)
    m = dict(comment=comment, ktype=ktype, vtype=vtype, map=d)
    if len(itypes) == len(d) and len(set(itypes.values())) == 1:
        m[ITYPE] = itypes.popitem()[1] # all use same non-str key
    elif itypes:
        m[ITYPES] = itypes
    return {JSON_MAP: m}


def json_to_uxf(config):
    filename = config.infiles[0]
    with open(filename, 'rt', encoding=UTF8) as file:
        data = json.load(file, object_hook=_json_naturalize)
    custom = data.get(JSON_CUSTOM)
    ttypes = None
    ttype_list = data.get(JSON_TTYPES)
    if ttype_list:
        ttypes = {}
        for ttype in ttype_list:
            ttypes[ttype.name] = ttype
    data = data.get(JSON_DATA)
    uxf.dump(config.outfile, uxf.Uxf(data, custom, ttypes=ttypes))


def _json_naturalize(d):
    if JSON_DATETIME in d:
        return uxf.naturalize(d[JSON_DATETIME])
    if JSON_DATE in d:
        return uxf.naturalize(d[JSON_DATE])
    if JSON_BYTES in d:
        return bytes.fromhex(d[JSON_BYTES])
    if JSON_LIST in d:
        jlist = d[JSON_LIST]
        ls = uxf.List(jlist[LIST])
        ls.comment = jlist[COMMENT]
        ls.vtype = jlist[VTYPE]
        return ls
    if JSON_MAP in d:
        jmap = d[JSON_MAP]
        itype = jmap.get(ITYPE) # str or None
        itypes = jmap.get(ITYPES) # dict or None
        m = uxf.Map()
        m.comment = jmap[COMMENT]
        m.ktype = jmap[KTYPE] # str or None
        m.vtype = jmap[VTYPE] # str or None
        for key, value in jmap[MAP].items():
            if itypes is not None:
                itype = itypes.get(key)
            if itype == BYTES:
                key = bytes.fromhex(key)
            else:
                key = key if itype is None else uxf.naturalize(key)
            m[key] = value
        return m
    if JSON_TABLE in d:
        jtable = d[JSON_TABLE]
        fields = [uxf.Field(name, vtype) for name, vtype in
                  jtable[FIELDS].items()]
        return uxf.Table(name=jtable[NAME], comment=jtable[COMMENT],
                         fields=fields, records=jtable[RECORDS])
    if JSON_TTYPE in d:
        fields = [uxf.Field(name, vtype) for name, vtype in
                  d[JSON_TTYPE][FIELDS].items()]
        return uxf.TType(d[JSON_TTYPE][NAME], fields)
    return d


def ini_to_uxf(config):
    ini = configparser.ConfigParser()
    filename = config.infiles[0]
    ini.read(filename)
    data = uxf.Map()
    for section in ini:
        d = ini[section]
        if d:
            m = data[section] = uxf.Map()
            for key, value in d.items():
                m[uxf.naturalize(key)] = uxf.naturalize(value)
    uxf.dump(config.outfile, uxf.Uxf(data, filename),
             one_way_conversion=True)


def uxf_to_sqlite(config):
    data, _ = uxf.load(config.infiles[0])
    if isinstance(data, uxf.Table):
        _uxf_to_sqlite(config, [data])
    elif (isinstance(data, (list, uxf.List)) and data and
            all(isinstance(v, uxf.Table) for v in data)):
        _uxf_to_sqlite(config, data)
    else:
        raise SystemExit('can only convert a UXF containing a single table '
                         'or a single list of Tables to SQLite')


def _uxf_to_sqlite(config, tables):
    sqlite3.register_adapter(bool, lambda b: 'TRUE' if b else 'FALSE')
    sqlite3.register_adapter(datetime.date, lambda d: d.isoformat())
    sqlite3.register_adapter(datetime.datetime, lambda d: d.isoformat())
    db = None
    try:
        db = sqlite3.connect(config.outfile)
        for table_index, table in enumerate(tables, 1):
            table_name = _create_table(db, table, table_index)
            _populate_table(db, table, table_name)
    finally:
        if db is not None:
            db.commit()
            db.close()


def _create_table(db, table, table_index):
    table_name = uxf.canonicalize(table.name, f'T_{table_index}')
    sql = ['CREATE TABLE IF NOT EXISTS ', table_name, ' (']
    types = ['TEXT'] * len(table.fieldnames)
    if table.records:
        for i, value in enumerate(table.records[0]):
            if isinstance(value, float):
                types[i] = 'REAL'
            elif isinstance(value, int) and not isinstance(value, bool):
                types[i] = 'INT'
            elif isinstance(value, (bytes, bytearray)):
                types[i] = 'BLOB'
    sep = ''
    for i, name in enumerate(table.fieldnames):
        field_name = uxf.canonicalize(name, f'F_{i + 1}')
        sql += [sep, field_name, ' ', types[i]]
        sep = ', '
    sql += [');']
    cursor = db.cursor()
    cursor.execute(''.join(sql))
    return table_name


def _populate_table(db, table, table_name):
    sql = ['INSERT INTO ', table_name, ' VALUES (',
           ', '.join('?' * len(table.fieldnames)), ');']
    cursor = db.cursor()
    cursor.executemany(''.join(sql), table.records)


def sqlite_to_uxf(config):
    print('sqlite_to_uxf', config) # TODO


def uxf_to_xml(config):
    print('uxf_to_xml', config) # TODO


def xml_to_uxf(config):
    print('xml_to_uxf', config) # TODO


BYTES = 'bytes'
COMMENT = 'comment'
DOT_CSV = '.CSV'
DOT_INI = '.INI'
DOT_JSN = '.JSN'
DOT_JSON = '.JSON'
DOT_SQLITE = '.SQLITE'
DOT_UXF = '.UXF'
DOT_UXF_GZ = '.UXF.GZ'
DOT_XML = '.XML'
FIELDS = 'fields'
ITYPE = 'itype'
ITYPES = 'itypes'
JSON_CUSTOM = 'UXF^custom'
JSON_TTYPES = 'UXF^ttypes'
JSON_TTYPE = 'UXF^ttype'
JSON_DATA = 'UXF^data'
JSON_BYTES = 'UXF^bytes'
JSON_DATE = 'UXF^date'
JSON_DATETIME = 'UXF^datetime'
JSON_LIST = 'UXF^list'
JSON_MAP = 'UXF^map'
JSON_TABLE = 'UXF^table'
KTYPE = 'ktype'
LIST = 'list'
MAP = 'map'
NAME = 'name'
RECORDS = 'records'
UTF8 = 'utf-8'
UXF = 'uxf'
VTYPE = 'vtype'

PREFIX = '''
uxfconvert.py <infile.uxf[.gz]> <outfile.{csv,json,sqlite,xml}>
uxfconvert.py [-i|--indent=N] [-f|--fieldnames] \
<infile.{csv,ini,json,sqlite,xml}> <outfile.uxf[.gz]>
uxfconvert.py [-i|--indent=N] [-f|--fieldnames] \
<infile1.csv> [infile2.csv ... infileM.csv] <outfile.uxf[.gz]>

'''

USAGE = '''Converts to and from uxf format.

If the outfile is .uxf.gz, the output will be gzip compressed UXF.

Indent defaults to 2 (uxf's default); but can be set to any value 0-8.

If fieldnames is set and the infile(s) is(are) csv the first row of each
infile will be read as field (column) names; otherwise all rows will be
assumed to contain values.

To produce compact uxf output use a .gz suffix and -i0.

Converting from multiple csv files to uxf, the outfile will either be a
list of tables (if the fieldnames option is given), or a list of lists of
scalars otherwise. Converting from one csv file will produce a uxf with a
table (if fieldnames is set) or a list of lists of scalars. Converting from
uxf to csv can only be done if the uxf contains a single scalar table or a
single list of lists of scalars.

Converting from ini to uxf is purely for example purposes (e.g., ini
comments are dropped). In a real application (e.g., migrating from ini to
uxf), a custom ini parser would be needed. Converting uxf to ini is not
supported.

Converting sqlite to uxf only converts the sql tables and so won't
roundtrip. Converting uxf to sqlite is only supported if the uxf file is a
single scalar table or a list of scalar tables.

Converting from uxf to json and back (i.e., using uxfconvert.py's own json
format) roundtrips with perfect fidelity.

Converting from uxf to xml and back (i.e., using uxfconvert.py's own xml
format) roundtrips with perfect fidelity.

Support for uxf to uxf conversions is provided by the uxf.py module itself,
which can be run directly or via python, e.g., `uxf.py infile.uxf
outfile.uxf` or `python3 -m uxf infile.uxf outfile.uxf` with the same indent
and compression options as here, plus additional options (use uxf.py's -h or
--help for details).'''


if __name__ == '__main__':
    main()
