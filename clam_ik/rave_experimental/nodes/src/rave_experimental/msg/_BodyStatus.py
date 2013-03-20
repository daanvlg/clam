"""autogenerated by genmsg_py from BodyStatus.msg. Do not edit."""
import roslib.message
import struct


class BodyStatus(roslib.message.Message):
  _md5sum = "9d67177aea4c214587c878f7ce226d1f"
  _type = "rave_experimental/BodyStatus"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """string object_id
bool picked_up
float32 x
float32 y
float32 z
float32 errno

"""
  __slots__ = ['object_id','picked_up','x','y','z','errno']
  _slot_types = ['string','bool','float32','float32','float32','float32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.
    
    The available fields are:
       object_id,picked_up,x,y,z,errno
    
    @param args: complete set of field values, in .msg order
    @param kwds: use keyword arguments corresponding to message field names
    to set specific fields. 
    """
    if args or kwds:
      super(BodyStatus, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.object_id is None:
        self.object_id = ''
      if self.picked_up is None:
        self.picked_up = False
      if self.x is None:
        self.x = 0.
      if self.y is None:
        self.y = 0.
      if self.z is None:
        self.z = 0.
      if self.errno is None:
        self.errno = 0.
    else:
      self.object_id = ''
      self.picked_up = False
      self.x = 0.
      self.y = 0.
      self.z = 0.
      self.errno = 0.

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    @param buff: buffer
    @type  buff: StringIO
    """
    try:
      _x = self.object_id
      length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_B4f.pack(_x.picked_up, _x.x, _x.y, _x.z, _x.errno))
    except struct.error, se: self._check_types(se)
    except TypeError, te: self._check_types(te)

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    @param str: byte array of serialized message
    @type  str: str
    """
    try:
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.object_id = str[start:end]
      _x = self
      start = end
      end += 17
      (_x.picked_up, _x.x, _x.y, _x.z, _x.errno,) = _struct_B4f.unpack(str[start:end])
      self.picked_up = bool(self.picked_up)
      return self
    except struct.error, e:
      raise roslib.message.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    @param buff: buffer
    @type  buff: StringIO
    @param numpy: numpy python module
    @type  numpy module
    """
    try:
      _x = self.object_id
      length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_B4f.pack(_x.picked_up, _x.x, _x.y, _x.z, _x.errno))
    except struct.error, se: self._check_types(se)
    except TypeError, te: self._check_types(te)

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    @param str: byte array of serialized message
    @type  str: str
    @param numpy: numpy python module
    @type  numpy: module
    """
    try:
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.object_id = str[start:end]
      _x = self
      start = end
      end += 17
      (_x.picked_up, _x.x, _x.y, _x.z, _x.errno,) = _struct_B4f.unpack(str[start:end])
      self.picked_up = bool(self.picked_up)
      return self
    except struct.error, e:
      raise roslib.message.DeserializationError(e) #most likely buffer underfill

_struct_I = roslib.message.struct_I
_struct_B4f = struct.Struct("<B4f")