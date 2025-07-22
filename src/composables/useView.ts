import { createSharedComposable } from '@vueuse/core'
import { ref } from 'vue'

type Views = 'chat' | 'models'

export const useView = createSharedComposable(() => {
  const activeView = ref<Views>('chat')

  const toggleView = (view: Views) => {
    activeView.value = view
  }

  return {
    activeView,
    toggleView,
  }
})
