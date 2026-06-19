/**
 * language-advisor 前端插件入口（v0.1 主库仍用通用 LabView；本文件供 register-plugins 与未来动态加载）
 */
export const plugin = {
  id: 'edu.hot.language-advisor',
  title: 'Smart Contract Language Advisor',
  routePrefix: '/labs/edu.hot.language-advisor',
  routes: [{ path: '', component: () => import('./LanguageAdvisorLab.vue') }],
  apiBase: '/api/v1/labs/edu.hot.language-advisor',
}

export default plugin
