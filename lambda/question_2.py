items = [123, 'abc', 456, 'def']

check_type = lambda item: 'Integer' if isinstance(item, int) else 'String'

result = list(map(check_type, items))
print(result)
