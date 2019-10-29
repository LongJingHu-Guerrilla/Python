# 类名: Const
# 描述：自定义常量类，用于补充python默认不支持常量的缺陷，常量命名必须全为大写字母
# 作者：Uncle Lv
# 日期：2019.10.29

class Const():
    class ConstError(TypeError):
        pass

    class ConstNameError(ConstError):
        pass

    def __setattr__(self, key, value):
        if key in self.__dict__.keys():
            raise self.ConstError("Can't change the value of the constant: " + '\'' + key + '\'')

        if not key.isupper():
            raise self.ConstNameError("The constant must be named with upper letters: " + '\'' + key + '\'')

        self.__dict__[key] = value
