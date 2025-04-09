const express = require('express')
const fs = require('fs')
const app = express()
const PORT = 80 // ou autre port

app.use(express.json())

app.post('/collect', (req, res) => {
  const { x, y, time } = req.body

  if (typeof x !== 'number' || typeof y !== 'number' || typeof time !== 'number') {
    return res.status(400).send('Invalid payload')
  }

  const logLine = `${x},${y},${time.toFixed(4)}\n`
  fs.appendFile('pixels_log.txt', logLine, err => {
    if (err) {
      console.error('Erreur lors de l\'écriture :', err)
      return res.status(500).send('Erreur serveur')
    }
    res.status(200).send('OK')
  })
})

app.listen(PORT, () => {
  console.log(`Serveur en écoute sur http://localhost:${PORT}/collect`)
})
