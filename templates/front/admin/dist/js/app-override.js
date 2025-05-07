// 覆盖登录页面标题
document.addEventListener('DOMContentLoaded', function() {
  // 立即替换一次
  replaceText();
  
  // 延迟执行以确保Vue已经渲染完成
  setTimeout(replaceText, 500);
  // 再次延迟执行确保动态加载的内容也被替换
  setTimeout(replaceText, 1500);
  
  function replaceText() {
    // 替换页面上所有包含原标题的文本节点
    var textWalker = document.createTreeWalker(
      document.body,
      NodeFilter.SHOW_TEXT,
      { acceptNode: function(node) { return NodeFilter.FILTER_ACCEPT; } },
      false
    );
    
    var node;
    while(node = textWalker.nextNode()) {
      if (node.nodeValue && node.nodeValue.includes('中国传统手工艺销售平台')) {
        node.nodeValue = node.nodeValue.replace(/中国传统手工艺销售平台/g, '工艺品交易系统');
      }
    }
    
    // 修改登录页标题
    var loginTitle = document.querySelector('.title-container .title');
    if (loginTitle) {
      loginTitle.textContent = '工艺品交易系统';
      // 确保没有其他样式干扰
      loginTitle.style.position = 'relative';
      loginTitle.style.zIndex = '2';
    }
    
    // 修改注册页标题
    var registerTitle = document.querySelector('.h1');
    if (registerTitle) {
      registerTitle.textContent = '工艺品交易系统注册';
      registerTitle.style.position = 'relative';
      registerTitle.style.zIndex = '2';
    }
    
    // 修改顶部导航栏标题
    var headerTitles = document.querySelectorAll('header h1, .navbar-brand, header .title');
    headerTitles.forEach(function(el) {
      if (el && el.textContent.includes('中国传统手工艺销售平台')) {
        el.textContent = '工艺品交易系统';
        el.style.position = 'relative';
        el.style.zIndex = '2';
      }
    });
    
    // 修改页面内的欢迎文本
    var welcomeText = document.querySelectorAll('h2, h3, h4, .welcome-text');
    welcomeText.forEach(function(el) {
      if (el && el.textContent.includes('中国传统手工艺销售平台')) {
        el.textContent = el.textContent.replace(/中国传统手工艺销售平台/g, '工艺品交易系统');
        el.style.position = 'relative';
        el.style.zIndex = '2';
      }
    });
    
    // 确保登录按钮可见
    var loginButton = document.querySelector('.loginInBt');
    if (loginButton) {
      loginButton.style.display = 'block';
      loginButton.style.visibility = 'visible';
      loginButton.style.backgroundColor = '#409EFF';
      loginButton.style.color = 'white';
      loginButton.style.borderRadius = '4px';
      loginButton.style.height = '40px';
      loginButton.style.margin = '10px 0 20px 0';
      loginButton.style.cursor = 'pointer';
    }
  }
}); 