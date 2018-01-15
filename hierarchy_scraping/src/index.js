const baseURL = 'https://www.tbs-sct.gc.ca/pol/'

function processNode(node, vertices = [], edges = [], parent = 0) {
  let childUL = node.querySelector('ul.tv-ul')
  let details = node.querySelector('a.tv-in')
  vertices.push({
    id: details.id,
    title: details.textContent,
    url: baseURL + details.href,
  })
  if (parent !== 0) {
    edges.push({
      _to: parent,
      _from: details.id,
    })
  }
  if (childUL) {
		// For some reason getting all the li in the whole tree
		// and then checking each to see if they are direct children
		// is faster than getting direct children and checking to see
		// if it's an LI. ¯\_(ツ)_/¯
    let children = childUL.querySelectorAll('li.tv-li')

    Array.from(children).forEach(child => {
      if (child.parentNode === childUL) {
        processNode(child, vertices, edges, details.id)
      }
    })
  }
  return { vertices, edges }
}

module.exports.processNode = processNode
