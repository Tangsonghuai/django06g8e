// Vue应用数据补丁
(function() {
  // 在DOM加载完成后执行
  document.addEventListener('DOMContentLoaded', function() {
    // 立即替换一次
    replaceElementsText();
    
    // 延迟执行以确保Vue动态内容已经渲染
    setTimeout(replaceElementsText, 500);
    setTimeout(replaceElementsText, 1500);
    
    // 监听DOM变化，对新添加的元素进行文本替换
    var observer = new MutationObserver(function(mutations) {
      replaceElementsText();
    });
    
    // 开始观察document.body的子树变化
    observer.observe(document.body, { 
      childList: true, 
      subtree: true,
      characterData: true,
      characterDataOldValue: true
    });
  });
  
  // 替换XHR响应中的文本
  var originalXHR = window.XMLHttpRequest.prototype.open;
  window.XMLHttpRequest.prototype.open = function() {
    this.addEventListener('load', function() {
      try {
        if (this.responseText && this.responseText.includes("中国传统手工艺销售平台")) {
          console.log("Patching response data...");
          Object.defineProperty(this, 'responseText', {
            get: function() {
              var patchedText = this._responseText || this.responseText;
              return patchedText.replace(/中国传统手工艺销售平台/g, "工艺品交易系统");
            }
          });
        }
      } catch (e) {
        console.error("Error in XHR patch:", e);
      }
    });
    originalXHR.apply(this, arguments);
  };
  
  // 替换页面上所有文本节点中的内容
  function replaceElementsText() {
    // 替换页面标题
    if (document.title.includes("中国传统手工艺销售平台")) {
      document.title = document.title.replace(/中国传统手工艺销售平台/g, "工艺品交易系统");
    }
    
    // 替换所有文本节点
    var walker = document.createTreeWalker(
      document.body,
      NodeFilter.SHOW_TEXT,
      { acceptNode: function(node) { return NodeFilter.FILTER_ACCEPT; } },
      false
    );
    
    var node;
    var textNodes = [];
    
    while(node = walker.nextNode()) {
      if (node.nodeValue && node.nodeValue.includes("中国传统手工艺销售平台")) {
        node.nodeValue = node.nodeValue.replace(/中国传统手工艺销售平台/g, "工艺品交易系统");
      }
    }
    
    // 特别处理可能有问题的元素
    var specialElements = document.querySelectorAll('h1, h2, h3, h4, h5, .title, header *');
    specialElements.forEach(function(el) {
      if (el.textContent && el.textContent.includes("中国传统手工艺销售平台")) {
        el.textContent = el.textContent.replace(/中国传统手工艺销售平台/g, "工艺品交易系统");
        // 确保文本显示正常
        el.style.position = 'relative';
        el.style.zIndex = '2';
        // 修复可能的文本叠加问题
        el.style.textShadow = 'none';
        el.style.background = 'none';
      }
    });
    
    // 处理欢迎页面的大标题
    var welcomeTitle = document.querySelector('.welcome-text, .center-text');
    if (welcomeTitle && welcomeTitle.textContent.includes("中国传统手工艺销售平台")) {
      welcomeTitle.innerHTML = welcomeTitle.innerHTML.replace(/中国传统手工艺销售平台/g, "<span style='position:relative;z-index:2;'>工艺品交易系统</span>");
    }
  }
})(); 