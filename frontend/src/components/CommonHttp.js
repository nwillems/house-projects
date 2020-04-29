import axios from 'axios'

export const HTTP = axios.create({
  baseURL: 'http://localhost:8000/',
  headers: {
    Authorization: 'Bearer {token}' // But auth should be a thing
  }
})

export const paginatedFetcher = function (url, setter) {
  HTTP.get(url)
    .then(response => {
      setter(response.data)

      if (response.data.next) {
        HTTP.fetchie(response.data.next, setter)
      }
    }).catch(e => { /* DO SOMETHING */ })
}
