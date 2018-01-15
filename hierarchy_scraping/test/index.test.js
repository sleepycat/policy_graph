const jsdom = require('jsdom')
const { JSDOM } = jsdom
const { processNode } = require('../src')
const { html } = require('./hierarchy.en')
const { ul } = require('./ul')

describe('parsing a tree', () => {
  it('can create dom from html', () => {
    const dom = new JSDOM(`<!DOCTYPE html><p>Hello world</p>`)
    const text = dom.window.document.querySelector('p').textContent
    expect(text).toEqual('Hello world')
  })

  it('returns an object with vertices and edges', () => {
    // [
    //   {
    //     id: 'id28230',
    //     title: 'Contractual Arrangements, Guidelines on',
    //     url: 'https://www.tbs-sct.gc.ca/pol/doc-eng.aspx?id=28230',
    //   },
    // ]
    const dom = new JSDOM(ul)
    const root = dom.window.document.querySelector('ul.tv-ul')
    let result = processNode(root)
    expect(result).toHaveProperty('vertices')
    expect(result).toHaveProperty('edges')
  })

  it('creates vertices and edges for the root and its children', () => {
    const dom = new JSDOM(ul)
    const root = dom.window.document.querySelector('li.tv-li')
    let result = processNode(root)
    expect(result.vertices.length).toEqual(3)
    expect(result.edges.length).toEqual(2)
  })

  it('can process the whole tree', () => {
    const dom = new JSDOM(html)
    const root = dom.window.document.querySelector('li.tv-li')
    let result = processNode(root)
    // console.log(JSON.stringify(result))
    expect(result.vertices.length).toEqual(221)
    expect(result.edges.length).toEqual(220)
  })
})
