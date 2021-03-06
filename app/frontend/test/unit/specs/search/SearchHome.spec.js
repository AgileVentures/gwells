import { shallowMount, createLocalVue } from '@vue/test-utils'
import Vuex from 'vuex'
import moxios from 'moxios'
import SearchHome from '@/registry/components/search/SearchHome'
import SearchTable from '@/registry/components/search/SearchTable'
import APIErrorMessage from '@/common/components/APIErrorMessage'
import fakeDrillerOptions from '../fakeDrillerOptions'
import { FETCH_CITY_LIST, FETCH_DRILLER_LIST, FETCH_DRILLER_OPTIONS } from '@/registry/store/actions.types'
import { SET_DRILLER_LIST } from '@/registry/store/mutations.types'

const localVue = createLocalVue()
localVue.use(Vuex)

describe('SearchHome.vue', () => {
  let store
  let getters
  let actions
  let mutations

  beforeEach(() => {
    moxios.install()
    getters = {
      drillerOptions: jest.fn().mockReturnValue(fakeDrillerOptions),
      drillers: () => {
        return {
          results: [
            {
              person_guid: '1e252dca-ccb9-439a-a6ec-aeec0f7e4a03',
              first_name: 'Alexis',
              surname: 'Rodriguez',
              organization_name: null,
              street_address: null,
              city: null,
              province_state: null,
              contact_tel: null,
              contact_email: null,
              activity: 'Well Driller',
              status: 'Active',
              registration_no: 'WD 08315530'
            },
            {
              person_guid: 'db02b5bb-1473-4f97-9bcf-f6214e8dd5aa',
              first_name: 'Ann',
              surname: 'Berg',
              organization_name: 'Earthplex Installers',
              street_address: '7010 Rocky Bluff Mall',
              city: 'Atlin',
              province_state: 'BC',
              contact_tel: '(604) 424-7090',
              contact_email: 'cardenas@driller.ca',
              activity: 'Well Driller',
              status: 'Active',
              registration_no: 'WD 04187177'
            }
          ]
        }
      },
      loading: () => false,
      listError: () => null,
      cityList: () => {
        return {
          drillers: [
            {
              cities: ['Duncan', 'Esquimalt'],
              prov: 'BC'
            },
            {
              prov: 'AB',
              cities: ['Jasper']
            }
          ],
          installers: [
            {
              cities: ['Nanaimo'],
              prov: 'BC'
            }
          ]
        }
      },
      userRoles: () => ({ registry: { edit: false, view: false, approve: false } }),
      activity: () => 'DRILL'
    }
    actions = {
      [FETCH_CITY_LIST]: jest.fn(),
      [FETCH_DRILLER_LIST]: jest.fn(),
      [FETCH_DRILLER_OPTIONS]: jest.fn()
    }
    mutations = {
      [SET_DRILLER_LIST]: jest.fn()
    }
    store = new Vuex.Store({ getters, actions, mutations })
  })

  afterEach(() => {
    moxios.uninstall()
  })

  it('loads the table component', () => {
    const wrapper = shallowMount(SearchHome, {
      store,
      localVue
    })
    expect(wrapper.findAll(SearchTable).length)
      .toEqual(1)
  })

  it('loads the error component if there is an error', () => {
    const getters = {
      drillers: () => [],
      loading: () => false,
      listError: () => {
        return { status: '400', statusText: 'error!' }
      },
      cityList: () => [],
      activity: () => 'DRILL',
      userRoles: () => ({ registry: { edit: false, view: false, approve: false } })
    }
    const store = new Vuex.Store({ getters, actions })
    const wrapper = shallowMount(SearchHome, {
      store,
      localVue
    })
    expect(wrapper.findAll(APIErrorMessage).length)
      .toEqual(1)
  })

  it('doesn\'t load the error component if there is no error', () => {
    const wrapper = shallowMount(SearchHome, {
      store,
      localVue
    })
    expect(wrapper.findAll(APIErrorMessage).length)
      .toEqual(0)
  })
  it('resets search params when reset button is clicked', () => {
    const wrapper = shallowMount(SearchHome, {
      store,
      localVue
    })
    wrapper.setData({
      searchParams: {
        search: 'Bob Driller',
        activity: 'PUMP',
        city: [''],
        status: 'INACTIVE',
        limit: '10',
        ordering: ''
      }
    })
    expect(wrapper.vm.searchParams).toEqual({
      search: 'Bob Driller',
      city: [''],
      activity: 'PUMP',
      status: 'INACTIVE',
      limit: '10',
      ordering: ''
    })
    wrapper.find('[type=reset]').trigger('reset')
    expect(wrapper.vm.searchParams).toEqual({
      search: '',
      city: [''],
      activity: 'DRILL',
      status: 'A',
      limit: '10',
      ordering: ''
    })
  })
  it('calls sort method when register table component emits a sort code', () => {
    const wrapper = shallowMount(SearchHome, {
      store,
      localVue
    })
    const table = wrapper.find(SearchTable)
    wrapper.vm.lastSearchedParams = wrapper.vm.searchParams
    table.vm.$emit('sort', 'surname')
    expect(wrapper.vm.lastSearchedParams.ordering).toEqual('-surname')
  })
  it('has a list of cities for drillers', () => {
    const wrapper = shallowMount(SearchHome, {
      store,
      localVue
    })
    const cityOptions = wrapper.findAll('#cityOptions option')
    expect(cityOptions.length).toEqual(4) // three options in store + 'all' option
    expect(cityOptions.at(0).text()).toEqual('All')
    expect(cityOptions.at(1).text()).toEqual('Duncan')
    expect(cityOptions.at(2).text()).toEqual('Esquimalt')
    expect(cityOptions.at(3).text()).toEqual('Jasper')
  })
  it('clears driller list when reset is clicked', () => {
    const wrapper = shallowMount(SearchHome, {
      store,
      localVue
    })
    wrapper.find('[type=reset]').trigger('reset')
    expect(mutations.SET_DRILLER_LIST).toHaveBeenCalled()
  })
})
