// 检测是否在登录页面上，如果是，则重定向到自动登录页面
(function() {
  // 判断当前是否在登录页面
  if (window.location.href.includes('index.html') && 
      !localStorage.getItem('Token') && 
      !window.location.hash) {
    // 重定向到自动登录页面
    window.location.href = 'login-direct.html';
  }
})(); 