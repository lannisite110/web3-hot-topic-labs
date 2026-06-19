export const plugin = {
  id: 'edu.hot.dao',
  title: 'DAO Vote Simulation Lab',
  routePrefix: '/labs/edu.hot.dao',
  routes: [{ path: '', component: () => import('./HotLab.vue') }],
  apiBase: '/api/v1/labs/edu.hot.dao',
}

export default plugin
