import { shallowMount, createLocalVue } from '@vue/test-utils'
import Vuex from 'vuex'
import VueRouter from 'vue-router'
import documentState from '@/common/store/documents.js'
import SubmissionsHome from '@/submissions/views/SubmissionsHome.vue'

import { FETCH_CODES, FETCH_WELLS } from '@/submissions/store/actions.types.js'

const localVue = createLocalVue()
localVue.use(Vuex)
localVue.use(VueRouter)

const router = new VueRouter()

describe('SubmissionsHome.vue', () => {
  let actions
  let store
  let getters

  beforeEach(() => {
    getters = {
      userRoles: () => ({ wells: { edit: true }, submissions: { edit: true } })
    }
    actions = {
      [FETCH_CODES]: jest.fn(),
      [FETCH_WELLS]: jest.fn()
    }
    store = new Vuex.Store({
      state: {},
      actions,
      getters,
      modules: { documentState }
    })
  })

  it('triggers confirmation box when submitting the form', () => {
    const wrapper = shallowMount(SubmissionsHome, {
      localVue,
      store,
      router,
      sync: false
    })
    expect(wrapper.vm.confirmSubmitModal).toEqual(false)

    wrapper.find('form').trigger('submit')

    expect(wrapper.vm.confirmSubmitModal).toEqual(true)
  })

  it('requests codes/constants to use in form', () => {
    shallowMount(SubmissionsHome, {
      localVue,
      store,
      router,
      sync: false
    })
    expect(actions[FETCH_CODES]).toHaveBeenCalled()
  })
})
