export const plugin = {
  id: 'edu.hot.zk-modular',
  title: 'ZK Modular Rollup Lab',
  routePrefix: '/labs/edu.hot.zk-modular',
  routes: [{ path: '', component: () => import('./HotLab.vue') }],
  apiBase: '/api/v1/labs/edu.hot.zk-modular',
}

export default plugin
