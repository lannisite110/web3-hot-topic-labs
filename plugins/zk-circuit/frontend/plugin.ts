export const plugin = {
  id: 'edu.hot.zk-circuit',
  title: 'ZK Circuit Compile Lab',
  routePrefix: '/labs/edu.hot.zk-circuit',
  routes: [{ path: '', component: () => import('./HotLab.vue') }],
  apiBase: '/api/v1/labs/edu.hot.zk-circuit',
}

export default plugin
