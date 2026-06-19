export const plugin = {
  id: 'edu.hot.mev',
  title: 'MEV PBS Simulation Lab',
  routePrefix: '/labs/edu.hot.mev',
  routes: [{ path: '', component: () => import('./HotLab.vue') }],
  apiBase: '/api/v1/labs/edu.hot.mev',
}

export default plugin
