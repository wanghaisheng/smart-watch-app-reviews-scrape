https://github.com/facundoolano/app-store-scraper


var store = require('app-store-scraper'); // regular non caching version
var memoized = require('app-store-scraper').memoized(); // cache with default options
var memoizedCustom = require('app-store-scraper').memoized({ maxAge: 1000 * 60 }); // cache with default options

memoized.app({id: 553834731}) // will make a request
  .then(() => memoized.app({id: 553834731})); // will resolve to the cached value without requesting



var store = require('app-store-scraper');

store.app({id: 553834731}).then(console.log).catch(console.log);


var store = require('app-store-scraper');

store.list({
  collection: store.collection.TOP_FREE_IPAD,
  category: store.category.GAMES_ACTION,
  num: 2
})
.then(console.log)
.catch(console.log);


var store = require('app-store-scraper');

store.search({
  term: 'panda',
  num: 2,
  page: 3,
  country : 'us',
  lang: 'lang'
})
.then(console.log)
.catch(console.log);


var store = require('app-store-scraper');

store.developer({devId: 284882218}).then(console.log).catch(console.log);


var store = require('app-store-scraper');

store.suggest({term: 'panda'}).then(console.log).catch(console.log);



var store = require('app-store-scraper');

store.reviews({
  appId: 'com.midasplayer.apps.candycrushsaga',
  sort: store.sort.HELPFUL,
  page: 2
})
.then(console.log)
.catch(console.log);


var store = require('app-store-scraper');

store.ratings({
  appId: 'com.midasplayer.apps.candycrushsaga',
})
.then(console.log)
.catch(console.log);


