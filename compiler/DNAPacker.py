import struct


# Byte orders...
LITTLE_ENDIAN = '<'
BIG_ENDIAN = '>'

# Data types...

# Signed integers...
INT8 = 'b'
INT16 = 'h'
INT32 = 'i'
INT64 = 'q'

# Unsigned integers...
UINT8 = 'B'
UINT16 = 'H'
UINT32 = 'I'
UINT64 = 'Q'

# Strings...
SHORT_STRING = 's'
LONG_STRING = 'S'

# Booleans...
BOOLEAN = '?'


class DNAPacker:
    def __init__(self, name='DNAPacker', packer=None, verbose=False):
        self.name = name
        self.__data = ''
        self.verbose = verbose

        # If we've been given either a DNAPacker object, or a string as an
        # argument for packer, let's use this as the starting point for our
        # data:
        if isinstance(packer, DNAPacker) or isinstance(packer, str):
            self.__data = str(packer)

    def __str__(self):
        return self.__data

    def __repr__(self):
        return repr(self.__data)

    def __len__(self):
        return len(self.__data)

    def __add__(self, other):
        if isinstance(other, self.__class__):
            other = str(other)
        return DNAPacker(name=self.name, packer=(self.__data + other),
                         verbose=self.verbose)

    def __radd__(self, other):
        if isinstance(other, self.__class__):
            other = str(other)
        return DNAPacker(name=self.name, packer=(other + self.__data),
                         verbose=self.verbose)

    def __iadd__(self, other):
        if isinstance(other, self.__class__):
            other = str(other)
        self.__data += other
        return self

    def debug(self, message):
        if self.verbose:
            print '{name}: {message}'.format(name=self.name, message=message)

    def pack(self, fieldName, value, dataType, byteOrder=LITTLE_ENDIAN):
        self.debug('packing... {fieldName}: {value}'.format(
                    fieldName=fieldName, value=repr(value)))

        # If we're packing a string, add the length header:
        if dataType == SHORT_STRING:
            self += struct.pack(UINT8, len(value))
        elif dataType == LONG_STRING:
            self += struct.pack(UINT16, len(value))

        if dataType in (SHORT_STRING, LONG_STRING):

            # Pack the data raw:
            self += value

        else:

            # Pack the value using struct.pack():
            self += struct.pack(byteOrder + dataType, value)
