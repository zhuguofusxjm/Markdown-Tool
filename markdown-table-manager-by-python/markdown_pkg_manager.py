import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import markdown
from markdown_utils import MarkdownUtils

class SoftwarePackage:
    """
    定义软件包元数据
    """
    def __init__(self, name, attributes=None, tags=None, dependencies=None):
        self.name = name
        self.attributes = attributes or {}
        self.tags = tags or []
        self.dependencies = dependencies or []

class PackageManager:
    def __init__(self):
        self.packages = {}
        self.all_define_tags = ["tag1", "tag2", "tag3", "tag4", "tag5", "tag6", "tag7", "tag8", "tag9", "tag10", "tag11",
                        "tag11", "tag12", "tag13", "tag14", "tag15", "tag16", "tag17", "tag18", "tag19", "tag20",
                        "tag21", "tag22", "tag23", "tag24", "tag25", "tag26", "tag27", "tag28", "tag29", "tag30"]
    def add_package(self, package):
        """
        添加软件包
        :param package:
        :return:
        """
        self.packages[package.name] = package

    def generate_md_table_content_lines(self):
        """
        生成markdown表格的内容
        :return:
        """
        _lines = []
        _line = "| Name | Attributes |"
        for tag in self.all_define_tags:
            _line = _line + f" {tag.capitalize()} |"
        _lines.append(_line)
        _line = "| --- | --- |"
        for _ in self.all_define_tags:
            _line = _line + (" --- |")
        _lines.append(_line)

        for name, package in self.packages.items():
            _line = ""
            _line = _line + "|"
            _line = _line + f" {name} |"
            _line = _line + f" {package.attributes} |"
            for tag in self.all_define_tags:
                if tag in package.tags:
                    _line = _line + f" Y |"
                else:
                    _line = _line + f" N |"
            _lines.append(_line)
        return _lines

    def display_packages(self):
        """
        显示软件包
        :return:
        """
        root = tk.Tk()
        root.title("Package Manager")
        # 创建表格
        tree = ttk.Treeview(root, columns=("Name", "Attributes", "Tags", "Dependencies"), show="headings")
        tree.heading("Name", text="Name")
        tree.heading("Attributes", text="Attributes")
        tree.heading("Tags", text="Tags")
        tree.heading("Dependencies", text="Dependencies")
        # 添加一些示例数据
        for name, package in self.packages.items():
            tree.insert("", "end", values=(name, str(package.attributes), str(package.tags), str(package.dependencies)))
        # 将表格放置在窗口中
        tree.pack(expand=True, fill="both")
        # 添加导出按钮
        export_button = tk.Button(root, text="Export", command=self.export_packages)
        export_button.pack()
        print(self.get_all_package_tags())
        root.mainloop()

    def get_all_package_tags(self):
        """
        获取所有标签信息
        :return:
        """
        # 获取所有标签
        tags = set()
        for name, package in self.packages.items():
            for tag in package.tags:
                tags.add(tag)
        return list(tags)

    def is_tag_valid(self):
        """
        判断所有的标签都应该在定义内
        :return:
        """
        # 获取所有标签
        tags = self.get_all_package_tags()
        is_sublist = all(elem in self.all_define_tags for elem in tags)
        if is_sublist:
            print("sub_list is a sublist of main_list")
        else:
            print("sub_list is not a sublist of main_list")
        return is_sublist

    def export_packages(self):
        lines = MarkdownUtils.align_md_table_columns(self.generate_md_table_content_lines())

        # 选择导出文件的路径
        file_path = ".//a.md"
        # file_path = filedialog.asksaveasfilename(defaultextension=".md", filetypes=[("Markdown files", "*.md")])

        # 将软件包信息写入Markdown文件
        if file_path:
            with open(file_path, "w") as file:
                file.write("# Package Manager\n\n")

                for line in lines:
                    file.write(line)
                    file.write("\n")




if __name__ == "__main__":
    # 创建一些软件包
    package1 = SoftwarePackage("Package1", {"version": "1.0"}, ["tag10",  "tag30"], ["Dependency1"])
    package2 = SoftwarePackage("Package2", {"version": "2.0"}, ["tag2", "tag3"], ["Dependency1", "Dependency2"])

    # 创建包管理器并添加软件包
    package_manager = PackageManager()
    package_manager.add_package(package1)
    package_manager.add_package(package2)

    # 显示软件包列表
    package_manager.display_packages()
    # package_manager.export_packages()

