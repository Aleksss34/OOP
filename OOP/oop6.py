class Note:
    raisee = ('до','ре','ми','фа','со','ля','си')
    def __init__(self, name, ton):
        
        self._name = name
        self._ton = ton
    def __setattr__(self, key, value):
        if key == '_name' and value not in self.raisee:
            raise ValueError('Недопустимое значение')
        if key == '_ton' and value not in (-1, 0, 1):
            raise ValueError('Недопустимое значение аргумента')
a = Note('до', 2)
class Notes:
    __slots__ = (_do, _re, _mi, _fa, _so, _la, _si)
    def __init__(self, _do, _re, _mi, _fa, _so, _la, _si )