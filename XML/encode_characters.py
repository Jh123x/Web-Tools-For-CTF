def to_xml_encode(letters):
    """Encodes a list of characters for XML"""
    return ''.join(list(map(lambda x: f'&#{ord(x)};', letters)))