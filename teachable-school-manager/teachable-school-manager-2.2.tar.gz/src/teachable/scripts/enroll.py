# coding: utf8
import argparse
import logging
import logging.config

import pyexcel as px

from ..api import Teachable
from ..course import Course
from ..user import User


def parse_arguments():
    parser = argparse.ArgumentParser(description='''Mass enroll users from Excel or CSV file into a specified course''',
                                     epilog="""---""")
    parser.add_argument('-i', '--input_file', nargs=1,
                        help='Excel or CSV file. The only needed columns are \'fullname\' and \'email\' ',
                        required=True)
    parser.add_argument('-c', '--courseId', type=str, nargs=1, help='The id of the course they should be enrolled in',
                        required=True)
    parser.add_argument('--dryrun', action='store_true',
                        default='False', help='''Don't do any actions for real, just do a dry run''')
    args = parser.parse_args()
    return args


def enroll_app(args):
    api = Teachable()
    logger = logging.getLogger(__name__)
    course_id = args.courseId[0]
    input_file = args.input_file[0]
    records = px.get_records(file_name=input_file)

    for user in records:
        # search if the user with the given email exists
        if user['email'] != '':
            u = User(api, user['email'])
            course = Course(api, course_id)
            if u.exists:
                if not args.dryrun:
                    resp = u.enroll(course)
                    if 'message' in resp.keys():
                        logger.info(resp['message'])
                    else:
                        logger.info(u.name + ' signed up!')
                else:
                    logger.info('[DRYRUN] Not enrolling for real {}'.format(u.name))
            else:
                logger.info('User {} doesn\'t exist. Creating and registering'.format(user['fullname']))
                # Add the user to the school and register to the course otherwise
                if not args.dryrun:
                    u.name = user['fullname']
                    resp = u.create(course)
                    if 'message' in resp.keys():
                        logger.info(resp['message'])
                else:
                    logger.info('[DRYRUN] Not creating for real {}'.format(u.name))



def main():
    args = parse_arguments()
    enroll_app(args)


if __name__ == '__main__':
    main()
