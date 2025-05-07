const base = {
    get() {
        return {
            url : "http://localhost:8080/django06g8e/",
            name: "django06g8e",
            // 退出到首页链接
            indexUrl: 'http://localhost:8080/front/index.html'
        };
    },
    getProjectName(){
        return {
            projectName: "工艺品交易系统"
        } 
    }
}
export default base
