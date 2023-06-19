/** @type {import('next').NextConfig} */
const nextConfig = {
  async redirects() {
    return [
      {
        source: '/init',
        destination: 'http://192.168.11.3:80/init',//change here
        permanent: false,
      },

      {
          source: '/graph',
          destination: 'http://192.168.11.3:80/test_graph',//change here
          permanent: false,
      },

      {
          source: '/:hash*',
          destination: 'http://192.168.11.3:80/:hash*',//change here
          permanent: false,
      },

    ]
  },
}

module.exports = nextConfig

// module.exports = {
//     async redirects() {
//       return [
//         {
//           source: '/init',
//           destination: 'http://192.168.11.3:80/init',//change here
//           permanent: true,
//         },

//         {
//             source: '/graph',
//             destination: 'http://192.168.11.3:80/test_graph',//change here
//             permanent: true,
//         },

//         {
//             source: '/:hash*',
//             destination: 'http://192.168.11.3:80/:hash*',//change here
//             permanent: true,
//         },

//       ]
//     },
//   }