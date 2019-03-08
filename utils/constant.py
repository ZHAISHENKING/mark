"""
常量Choice对照表
"""

# 常用字段类型
FIELD_CHOICE = dict([
    (0, "StringField"), (1, "IntField"),
    (2, "BooleanField"), (3, "DateTimeField"),
    (4, "EmbeddedDocumentField"), (5, "DynamicField"),
    (6, "ListField"), (7, "DictField"), (8, "MapField"),
    (9, "ReferenceField"), (10, "ImageField"), (11, "SequenceField"),
    (12, "UUIDField"), (13, "FileField"), (14, "BinaryField")
])