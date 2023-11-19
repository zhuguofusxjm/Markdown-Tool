// Vue 实例化
new Vue({
  el: '#app', // 将 Vue 实例挂载到 HTML 页面上 id 为 app 的元素上
  data: {
    // Vue 数据
    markdownContent: `| Name     | Attributes         | Tag1 | Tag2 |
|----------|--------------------|------|------|
| Package1 | {'version': '1.0'} | N    | N    |
| Package2 | {'version': '2.0'} | N    | Y    |`,
    tableData: [], // 存储 Markdown 表格解析后的数据
    tableHeaders: [], // 存储表头数据
    displayedData: [], // 存储显示的数据
    queryValues: [], // 存储查询条件
    editingCell: null, // 当前编辑的单元格位置
    editedValue: '', // 编辑后的值
    showAddLineModal: false, // 存储模态框中单行的显示开关
    newLineModalData: {}, // 存储模态框中单行的数据
    showAddColumnModal: false, // 存储模态框中单列的显示开关
    newColumnName: '', // 存储模态框中单列的列名
    newColumnDefaultValue: '' // 存储模态框中单列的默认值

  },
  //Vue 实例已经被挂载到了指定的元素上，可以进行 DOM 操作和数据初始化等工作。这个阶段通常用于执行一些初始化逻辑、绑定事件监听器、进行 API 请求或者其他需要在 Vue 实例挂载到页面之后执行的操作。
  mounted() {
    // Vue 实例挂载后执行的生命周期钩子函数
    this.parseMarkdownTable(); // 解析 Markdown 表格
  },
  methods: {
    // 解析 Markdown 表格
    parseMarkdownTable() {
      // Markdown 内容按行分割成数组
      const rows = this.markdownContent.split('\n');
      let tableStarted = false; //标记是否已经开始解析表格

      // 遍历每一行内容
      rows.forEach(row => {
        if (tableStarted) {
          // 如果已经开始解析表格，则按分隔符 '|' 分割单元格并存储
          const cells = row.split('|').filter(cell => cell.trim() !== '');
          this.tableData.push(cells.map(cell => cell.trim()));
        }

        if (row.includes('|---')) {
          // 如果遇到分隔符行，则表示表格开始
          tableStarted = true;
        }

        if (!tableStarted && row.includes('|')) {
          // 解析表头行
          const headers = row.split('|').filter(cell => cell.trim() !== '');
          this.tableHeaders = headers.map(header => header.trim());
          this.queryValues = Array(this.tableHeaders.length).fill('');
        }
      });

      // 设置显示的数据为解析后的数据
      this.displayedData = this.tableData.slice();
    },
    // 过滤表格数据
    filterTable() {
      // 根据查询条件对表格数据进行过滤
      // every() 函数是检查数组中的所有元素是否都满足指定的条件，如果所有元素都满足条件，则 every() 返回 true，否则返回 false
      // some() 函数检查数组中是否有至少一个元素满足指定条件。只要有一个元素通过测试函数，some() 就返回 true；
      const queryResult = this.tableData.filter(row => {
        return row.every((cell, index) => {
          const queryValue = this.queryValues[index].toLowerCase();
          return cell.toLowerCase().includes(queryValue);
        });
      });
      // 更新显示的数据为过滤结果
      this.displayedData = queryResult;
    },
    // 编辑表格单元格
    editCell(row, col) {
      // 设置当前编辑的单元格位置
      this.editingCell = { row, col };
      // 将编辑前的值赋给编辑框
      this.editedValue = this.displayedData[row][col];
    },
    // 保存编辑后的单元格值
    saveCell(row, col) {
      // 将编辑后的值保存到对应的 displayedData 中
      this.displayedData[row][col] = this.editedValue;
      // 关闭编辑状态
      this.editingCell = null;
    },
    // 取消编辑
    cancelEdit() {
      // 关闭编辑状态
      this.editingCell = null;
    },
    // 保存 Markdown 表格（逻辑待实现）
    saveMarkdownTable() {
      console.log('Table saved:', this.markdownContent);
      // TODO: 实现保存表格至另一个 Markdown 文件的逻辑
    },
    // 添加行
    addRow() {
      console.log('Adding a row');
      this.showAddLineModal = true
      // TODO: 实现添加行的逻辑
    },
    // 保存模态框中的数据
    saveNewLineModalData() {
      // 将模态框中的数据保存到 tableData 中
      this.tableData.push(Object.values(this.newLineModalData));
      // 更新显示的数据为 tableData
      this.displayedData = this.tableData.slice();
      // 关闭模态框
      this.showAddLineModal = false;
      // 清空 newLineModalData 对象
      this.newLineModalData = {};
    },
    // 添加列
    addColumn() {
        // 添加新列
      console.log('Adding a column');
      this.showAddColumnModal = true;
    },
    saveNewColumnModalData() {
      // 将新列名和默认值添加至表头和每一行数据
      this.tableHeaders.push(this.newColumnName);
      // 更新 queryValues 数组以匹配新的列数
      this.queryValues.push('');

      this.tableData.forEach(row => row.push(this.newColumnDefaultValue));

      // 更新显示的数据为更新后的数据
      this.displayedData = this.tableData.slice();
      // 关闭模态框
      this.showAddColumnModal = false;
      // 清空输入框内容
      this.newColumnName = '';
      this.newColumnDefaultValue = '';
    }
  }
});
