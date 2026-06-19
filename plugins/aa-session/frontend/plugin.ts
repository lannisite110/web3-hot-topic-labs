export const plugin = {
  id: 'edu.hot.aa-session',
  title: 'AA Session Key Lab',
  routePrefix: '/labs/edu.hot.aa-session',
  routes: [{ path: '', component: () => import('./HotLab.vue') }],
  apiBase: '/api/v1/labs/edu.hot.aa-session',
}

export default plugin
