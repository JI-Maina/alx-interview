#!/usr/bin/node

const request = require('request');
const filmId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${filmId}/`;

function getName (url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (response.statusCode === 200) {
        const data = JSON.parse(body);
        resolve(data.name);
      }

      if (error) {
        reject(new Error(response.statusCode));
      }
    });
  });
}

request(url, async (error, response, body) => {
  if (response.statusCode === 200) {
    const data = JSON.parse(body);
    const characters = data.characters;

    for (const url of characters) {
      const name = await getName(url);
      console.log(name);
    }
  }

  if (error) {
    console.error(error);
  }
});
