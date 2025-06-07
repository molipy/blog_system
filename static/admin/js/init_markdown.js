// 初始化 SimpleMDE 编辑器
// 在后台管理页面加载后执行
window.addEventListener('DOMContentLoaded', function () {
  var textarea = document.querySelector('.markdown-editor');
  if (textarea) {
    new SimpleMDE({ element: textarea });
  }
});
