export const plugin = {
  id: 'edu.hot.did',
  title: 'DID Privacy Demo Lab',
  routePrefix: '/labs/edu.hot.did',
  routes: [{ path: '', component: () => import('./HotLab.vue') }],
  apiBase: '/api/v1/labs/edu.hot.did',
}

export default plugin
