import { defineConfig } from 'vitepress'
import output from '../output.json'
// https://vitepress.dev/reference/site-config
export default defineConfig({
  title: "Tensorflow Questions",
  description: "Tensorflow questions",
  themeConfig: {
    // https://vitepress.dev/reference/default-theme-config
    nav: [
      { text: 'Home', link: '/' },
      { text: 'Questions', link: '/introduction' }
    ],

    sidebar: [
      {
        text: 'Examples',
        items: [
          ...output.filter(item => item.name !=='index').map((item) => {
            return { text: item.name, link: '/' + item.slug }
            
          })
        ]
      }
    ],

    socialLinks: [
      { icon: 'github', link: 'https://github.com/vuejs/vitepress' }
    ]
  }
})
