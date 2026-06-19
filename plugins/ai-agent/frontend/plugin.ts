export const plugin = {
  id: 'edu.hot.ai-agent',
  title: 'AI Agent Sandbox Lab',
  routePrefix: '/labs/edu.hot.ai-agent',
  routes: [{ path: '', component: () => import('./HotLab.vue') }],
  apiBase: '/api/v1/labs/edu.hot.ai-agent',
}

export default plugin
