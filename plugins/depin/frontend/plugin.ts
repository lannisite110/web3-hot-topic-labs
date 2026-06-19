export const plugin = {
  id: 'edu.hot.depin',
  title: 'DePIN Node Simulation Lab',
  routePrefix: '/labs/edu.hot.depin',
  routes: [{ path: '', component: () => import('./HotLab.vue') }],
  apiBase: '/api/v1/labs/edu.hot.depin',
}

export default plugin
