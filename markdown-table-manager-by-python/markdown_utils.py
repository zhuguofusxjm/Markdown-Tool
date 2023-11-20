import re

class MarkdownUtils:
    @staticmethod
    def align_md_table_columns(table_lines):
        """
        对齐md表格列
        :param table_lines:
        :return:
        """
        # 记录每列的最大宽度
        column_max_width_array = []
        # 初始化长度全为0
        for line in table_lines:
            splits = line.split('|')
            column_max_width_array = [0 for i in range(len(splits))]

        # 统计每列的最大字节数
        for line in table_lines:
            splits = line.split('|')
            for index, split in enumerate(splits):
                column_max_width_array[index] = max(column_max_width_array[index], len(split))
                print(column_max_width_array)

        # # 重新刷新每行，做补齐对齐
        new_lines = []
        for line in table_lines:
            _new_line = MarkdownUtils.auto_align_each_line(column_max_width_array, line)
            new_lines.append(_new_line)
        return new_lines

    @staticmethod
    def auto_align_each_line(column_max_width_array, line):
        """
        格式化每行数据，确保每列都按照最大字节数占位，不足使用空格补齐
        :param column_max_width_array:
        :param line:
        :return:
        """
        _new_line = ""
        splits = line.split('|')
        for index, split in enumerate(splits):
            _column_val = split.strip()
            _column_val_width = len(_column_val)
            _expect_max_width = column_max_width_array[index]

            if _column_val_width == _expect_max_width:
                _new_line = _new_line + _column_val
            else:
                # 重做表头
                if MarkdownUtils.is_md_table_header(line):
                    for i in range(_expect_max_width):
                        _new_line = _new_line + "-"
                else:
                    # 重做内容
                    _new_line = _new_line + " " + _column_val
                    for i in range(_expect_max_width - _column_val_width - 2):
                        _new_line = _new_line + " "
                    _new_line = _new_line + " "
            if index != len(splits) - 1:
                _new_line = _new_line + '|'
        return _new_line

    @staticmethod
    def read_md_content_from_file(file):
        with open(file, "r", encoding="utf-8") as file:
            md_content = file.read()
        return md_content

    @staticmethod
    def write_md_content_into_file(file, content):
        with open(file, "w", encoding="utf-8") as file:
            file.write(content)

    @staticmethod
    def convert_to_lines(md_content):
        """
        拆分Markdown文本为行
        :param md_content:
        :return:
        """
        lines = md_content.split('\n')
        return lines

    @staticmethod
    def is_md_table_content(line):
        """
        匹配md表格行
        :param md_content:
        :return:
        """
        # 匹配表格行的正则表达式
        table_row_pattern = re.compile(r'\|(.+?)\|')
        if re.match(table_row_pattern, line):
            return True
        else:
            return False

    @staticmethod
    def is_md_table_header(line):
        """
        匹配Markdown表格的表头格式
        :param line:
        :return:
        """
        md_table_header_pattern = re.compile(r'^\|(\s*---\s*\|)+$')
        if re.match(md_table_header_pattern, line):
            return True
        else:
            return False


#

# if __name__ == "__main__":
#     # 读取Markdown文件内容
#     with open("a.md", "r", encoding="utf-8") as file:
#         md_content = file.read()
#
#     # 对齐表格列
#     aligned_md_content = align_table_columns(md_content)
#
#     # 将对齐后的内容写回文件
#     with open("b.md", "w", encoding="utf-8") as file:
#         file.write(aligned_md_content)