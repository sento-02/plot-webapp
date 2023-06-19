/** @type {import('next').NextConfig} */
const nextConfig = {
  async rewrites() {
    return [
      {
        source: '/init',
        destination: 'http://192.168.11.3:80/init',//change here
      },

      {
          source: '/graph',
          destination: 'http://192.168.11.3:80/test_graph',//change here
      },

      {
          source: '/:hash*',
          destination: 'http://192.168.11.3:80/:hash*',//change here
      },

    ]
  },
}

module.exports = nextConfig