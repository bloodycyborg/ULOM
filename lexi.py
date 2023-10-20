import re
import keyword

class Token:
    def __init__(self, token_type, value):
        self.token_type = token_type
        self.value = value

class Lexer:
    def __init__(self, source_code):
        with open(file_path, 'r') as file:
            self.source_code = file.read()
        self.tokens = []

    def analyze(self):
        source_code = self.source_code
        keywords = set(keyword.kwlist)

        while source_code:
            if source_code.startswith('"') or source_code.startswith("'"):
                string_delimiter = source_code[0]
                end_index = source_code.find(string_delimiter, 1)
                if end_index == -1:
                    raise Exception("Unclosed string")
                string_literal = source_code[1:end_index]
                self.tokens.append(Token('STRING', string_literal))
                source_code = source_code[end_index + 1:]
            elif re.match(r'^[a-zA-Z_]\w*', source_code):
                identifier = re.match(r'^[a-zA-Z_]\w*', source_code).group(0)
                if identifier in keywords:
                    self.tokens.append(Token('KEYWORD', identifier))
                else:
                    self.tokens.append(Token('IDENTIFIER', identifier))
                source_code = source_code[len(identifier):]
            elif re.match(r'^\d+', source_code):
                number = re.match(r'^\d+', source_code).group(0)
                self.tokens.append(Token('NUMBER', int(number)))
                source_code = source_code[len(number):]
            elif re.match(r'^[+\-*/=<>!]+', source_code):
                operator = re.match(r'^[+\-*/=<>!]+', source_code).group(0)
                self.tokens.append(Token('OPERATOR', operator))
                source_code = source_code[len(operator):]
            elif source_code[0].isspace():
                source_code = source_code[1:]
            else:
                punctuation = source_code[0]
                self.tokens.append(Token('PUNCTUATION', punctuation))
                source_code = source_code[1:]

        return self.tokens

if __name__ == '__main__':

    file_path = "functions.py"
    lexer = Lexer(file_path)
    tokens = lexer.analyze()

    max_type_len = max(len(token.token_type) for token in tokens)

    print("Token Type".ljust(max_type_len + 5), "Value")
    print("-" * (max_type_len + 5), "-----")

    for token in tokens:
        print(token.token_type.ljust(max_type_len + 5), token.value)
