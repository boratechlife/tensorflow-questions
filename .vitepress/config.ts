import { defineConfig } from 'vitepress'
import output from '../output.json'
// https://vitepress.dev/reference/site-config

function convertSlugToText(slug: string) {
  const words = slug.split('-');
  const capitalizedWords = words.map(word => word.charAt(0).toUpperCase() + word.slice(1));
  const text = capitalizedWords.join(' ');
  return text;
}

export default defineConfig({
  title: "Tensorflow Questions",
  description: "Tensorflow questions",
  themeConfig: {
    // https://vitepress.dev/reference/default-theme-config
    nav: [
      { text: 'Home', link: '/' },
      { text: 'Questions', link: '/tensorflow/introduction' }
    ],

    sidebar: [
      {
        text: 'Examples',
        items: [
          ...output.filter(item => item.name !=='index').map((item) => {
            return { text: convertSlugToText(item.slug), link: '/tensorflow/' + item.slug }
            
          })
        ]
      }
    ],

    socialLinks: [
      { icon: 'github', link: 'https://github.com/vuejs/vitepress' }
    ]
  }
})
