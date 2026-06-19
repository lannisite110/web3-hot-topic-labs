export const plugin = {
  id: 'edu.hot.rwa-edu',
  title: 'RWA Education Simulation Lab',
  routePrefix: '/labs/edu.hot.rwa-edu',
  routes: [{ path: '', component: () => import('./HotLab.vue') }],
  apiBase: '/api/v1/labs/edu.hot.rwa-edu',
}

export default plugin
