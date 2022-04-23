"""Functions for working with IP addresses."""
import ipaddress
from operator import attrgetter
from netutils.constants import IPV4_MASKS, IPV6_MASKS


def ipaddress_address(ip, attr):
    """Convenience function primarily built to expose ipaddress.ip_address to Jinja.

    Args:
        ip_addr (str): IP Address str compliant with ipaddress.ip_address inputs.
        attr (atr): An attribute in string dotted format.

    Returns:
        str: Returns the value provided by the ipaddress.ip_address attribute provided.

    Example:
        >>> from netutils.ip import ipaddress_address
        >>> ipaddress_address('10.1.1.1', 'version')
        4
        >>> ipaddress_address('10.1.1.1', '__int__')
        167837953
        >>> ipaddress_address('10.1.1.1', 'is_loopback')
        False
        >>>
    """
    retriever = attrgetter(attr)
    retrieved_method = retriever(ipaddress.ip_address(ip))
    if callable(retrieved_method):
        return retrieved_method()
    return retrieved_method


def ipaddress_interface(ip, attr):
    """Convenience function primarily built to expose ipaddress.ip_interface to Jinja.

    Args:
        ip_interface (str): IP interface str compliant with ipaddress.ip_interface inputs.
        attr (atr): An attribute in string dotted format.

    Returns:
        str: Returns the value provided by the ipaddress.ip_interface attribute provided.

    Example:
        >>> from netutils.ip import ipaddress_interface
        >>> ipaddress_interface('10.1.1.1/24', 'version')
        4
        >>> ipaddress_interface('10.1.1.1/24', '__int__')
        167837953
    """
    retriever = attrgetter(attr)
    retrieved_method = retriever(ipaddress.ip_interface(ip))
    if callable(retrieved_method):
        return retrieved_method()
    return retrieved_method


def ipaddress_network(ip, attr):
    """Convenience function primarily built to expose ipaddress.ip_network to Jinja.

    Args:
        ip_network (str): IP network str compliant with ipaddress.ip_network inputs.
        attr (atr): An attribute in string dotted format.

    Returns:
        str: Returns the value provided by the ipaddress.ip_network attribute provided.

    Example:
        >>> from netutils.ip import ipaddress_network
        >>> ipaddress_network('10.1.1.0/24', 'version')
        4
        >>> ipaddress_network('10.1.1.0/24', '__str__')
        '10.1.1.0/24'
        >>>
    """
    retriever = attrgetter(attr)
    retrieved_method = retriever(ipaddress.ip_network(ip))
    if callable(retrieved_method):
        return retrieved_method()
    return retrieved_method


def ip_to_hex(ip):
    """Converts an IP address in string format to a hex string.

    Args:
        ip (str): An IP address in string format that is able to be converted by `ipaddress` library.

    Returns:
        str: HEX value of the IP address.

    Example:
        >>> from netutils.ip import ip_to_hex
        >>> ip_to_hex("10.100.100.100")
        '0a646464'
        >>>
    """
    ip_obj = ipaddress.ip_address(ip)
    return str(hex(int(ip_obj)))[2:].zfill(int(ip_obj.max_prefixlen / 4))


def ip_addition(ip, val):
    """Adds an integer to an IP address.

    Args:
        ip (str): An IP address in string format that is able to be converted by `ipaddress` library.
        val (int): An integer of which the IP address should be added by.

    Returns:
        str: IP address formatted string with the newly added IP address.

    Example:
        >>> from netutils.ip import ip_addition
        >>> ip_addition("10.100.100.100", 200)
        '10.100.101.44'
        >>>
    """
    return str(ipaddress.ip_address(ip) + val)


def ip_to_bin(ip):
    """Converts an IP address in string format to a binary string.

    Args:
        ip (str): An IP address in string format that is able to be converted by `ipaddress` library.

    Returns:
        str: Binary value of the IP address.

    Example:
        >>> from netutils.ip import ip_to_bin
        >>> ip_to_bin("10.100.100.100")
        '00001010011001000110010001100100'
        >>>
    """
    ip_obj = ipaddress.ip_address(ip)
    return bin(int(ip_obj))[2:].zfill(ip_obj.max_prefixlen)


def ip_subtract(ip, val):
    """Subtract an integer to an IP address.

    Args:
        ip (str): An IP address in string format that is able to be converted by `ipaddress` library.
        val (int): An integer of which the IP address should be subtracted by.

    Returns:
        str: IP address formatted string with the newly subtracted IP address.

    Example:
        >>> from netutils.ip import ip_subtract
        >>> ip_subtract("10.100.100.100", 200)
        '10.100.99.156'
        >>>
    """
    return str(ipaddress.ip_address(ip) - val)


def is_ip(ip):
    """Verifies whether or not a string is a valid IP address.

    Args:
        ip (str): An IP address in string format that is able to be converted by `ipaddress` library.

    Returns:
        bool: The result as to whether or not the string is a valid IP address.

    Example:
        >>> from netutils.ip import is_ip
        >>> is_ip("10.100.100.256")
        False
        >>> is_ip("10.100.100.255")
        True
        >>>
    """
    try:
        ip = ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False


def is_netmask(netmask):
    """Verifies whether or not a string is a valid subnet mask.

    Args:
        netmask (str): A subnet mask in

    Returns:
        bool: True if string is a valid subnet mask. Otherwise, false.

    Example:
        >>> from netutils.ip import is_netmask
        >>> is_netmask('255.255.255.0')
        True
        >>> is_netmask('24')
        False
        >>> is_netmask('255.255.266.0')
        False
    """
    try:
        return int(ipaddress.ip_address(netmask)) in IPV4_MASKS or int(ipaddress.ip_address(netmask)) in IPV6_MASKS
    except ValueError:
        return False


def netmask_to_cidr(netmask):
    """Creates a CIDR notation of a given subnet mask in decimal format.

    Args:
        netmask (str): A subnet mask in decimal format.

    Returns:
      cidr (str): CIDR representation of subnet mask.

    Example:
        >>> from netutils.ip import netmask_to_cidr
        >>> netmask_to_cidr("255.255.255.0")
        24
        >>> netmask_to_cidr("255.255.254.0")
        23
    """
    if is_netmask(netmask):
        return bin(int(ipaddress.ip_address(netmask))).count("1")
    raise ValueError("Subnet mask is not valid.")


def cidr_to_netmask(cidr):
    """Creates a decimal format of a CIDR value.

    **IPv4** only.  For IPv6, please use `cidr_to_netmaskv6`.

    Args:
        cidr (int): A CIDR value.

    Returns:
      netmask (str): Decimal format representation of CIDR value.

    Example:
        >>> from netutils.ip import cidr_to_netmask
        >>> cidr_to_netmask(24)
        '255.255.255.0'
        >>> cidr_to_netmask(17)
        '255.255.128.0'
    """
    if isinstance(cidr, int) and 0 <= cidr <= 32:
        return ".".join([str((0xFFFFFFFF << (32 - cidr) >> i) & 0xFF) for i in [24, 16, 8, 0]])
    raise ValueError("Parameter must be an integer between 0 and 32.")


def cidr_to_netmaskv6(cidr):
    """Creates a decimal format of a CIDR value.

    Args:
        cidr (int): A CIDR value.

    Returns:
      netmask (str): Decimal format (IPv6) representation of CIDR value.

    Example:
        >>> from netutils.ip import cidr_to_netmaskv6
        >>> cidr_to_netmaskv6(24)
        'ffff:ff00::'
        >>> cidr_to_netmaskv6(17)
        'ffff:8000::'
    """
    if isinstance(cidr, int) and 0 <= cidr <= 128:
        return str(ipaddress.IPv6Address(((1 << cidr) - 1) << (128 - cidr)))
    raise ValueError("Parameter must be an integer between 0 and 128.")


def get_all_host(ip_network):
    """Given a network, return the list of usable IP addresses.

    Args:
        ip_network (str): An IP network in string format that is able to be converted by `ipaddress` library.

    Returns:
        generator: Generator of usable IP Addresses within network.

    Example:
        >>> from netutils.ip import get_all_host
        >>> print(list(get_all_host("10.100.100.0/29")))
        ['10.100.100.1', '10.100.100.2', '10.100.100.3', '10.100.100.4', '10.100.100.5', '10.100.100.6']
        >>>
    """
    return (str(ip) for ip in ipaddress.ip_network(ip_network).hosts())


def get_broadcast_address(ip_network):
    """Given a network, determine the broadcast IP address.

    Args:
        ip_network (str): An IP network in string format that is able to be converted by `ipaddress` library.

    Returns:
        str: IP address formatted string with the broadcast IP address in the network.

    Example:
        >>> from netutils.ip import get_broadcast_address
        >>> get_broadcast_address("10.100.0.0/16")
        '10.100.255.255'
        >>>
    """
    return str(ipaddress.ip_network(ip_network).broadcast_address)


def get_first_usable(ip_network):
    """Given a network, determine the first usable IP address.

    Args:
        ip_network (str): An IP network in string format that is able to be converted by `ipaddress` library.

    Returns:
        str: IP address formatted string with the first usable IP address in the network.

    Example:
        >>> from netutils.ip import get_first_usable
        >>> get_first_usable("10.100.0.0/16")
        '10.100.0.1'
        >>>
    """
    net = ipaddress.ip_network(ip_network)
    if net.prefixlen in [31, 127]:
        return str(net[0])
    return str(net[1])


def get_peer_ip(ip_interface):
    """Given an IP interface (an ip address, with subnet mask) that is on a peer network, return the peer IP.

    Args:
        ip_interface (str): An IP interface in string format that is able to be converted by `ipaddress` library.

    Returns:
        str: IP address formatted string with the corresponding peer IP.

    Example:
        >>> from netutils.ip import get_peer_ip
        >>> get_peer_ip('10.0.0.1/255.255.255.252')
        '10.0.0.2'
        >>> get_peer_ip('10.0.0.2/30')
        '10.0.0.1'
        >>> get_peer_ip('10.0.0.1/255.255.255.254')
        '10.0.0.0'
        >>> get_peer_ip('10.0.0.0/31')
        '10.0.0.1'
        >>>
    """
    ip_obj = ipaddress.ip_interface(ip_interface)
    if isinstance(ip_obj, ipaddress.IPv4Address) and ip_obj.network.prefixlen not in [30, 31]:
        raise ValueError(f"{ip_obj} did not conform to IPv4 acceptable masks of 30 or 31")
    if isinstance(ip_obj, ipaddress.IPv6Address) and ip_obj.network.prefixlen not in [126, 127]:
        raise ValueError(f"{ip_obj} did not conform to IPv6 acceptable masks of 126 or 127")
    if ip_obj.network.prefixlen in [30, 126] and ip_obj.ip in [
        ip_obj.network.network_address,
        ip_obj.network.broadcast_address,
    ]:
        raise ValueError(f"{ip_obj} is not an IP in the point-to-point link usable range.")
    # The host lists returns all usable IPs, remove the matching one, return the first element. This can be optimized greatly, but left
    # like this for simplicity. Note: IPv6 technically does not have a broadcast address, but for ptp, this is not considered.
    val = list(get_all_host(str(ip_obj.network)))
    val.remove(str(ip_obj.ip))
    return val[0]


def get_usable_range(ip_network):
    """Given a network, return the string of usable IP addresses.

    Args:
        ip_network (str): An IP network in string format that is able to be converted by `ipaddress` library.

    Returns:
        str: String of usable IP Addresses within network.

    Example:
        >>> from netutils.ip import get_usable_range
        >>> get_usable_range("10.100.100.0/29")
        '10.100.100.1 - 10.100.100.6'
        >>>
    """
    net = ipaddress.ip_network(ip_network)
    if net.prefixlen in [31, 127]:
        lower_bound = str(net[0])
        upper_bound = str(net[1])
    else:
        lower_bound = str(net[1])
        upper_bound = str(net[-2])
    return f"{lower_bound} - {upper_bound}"
