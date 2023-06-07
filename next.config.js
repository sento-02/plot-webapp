/** @type {import('next').NextConfig} */
const nextConfig = {}

module.exports = nextConfig

module.exports = {
    async rewrites() {
      return [
        {
          source: '/test/file_list',
          destination: 'http://10.100.53.90:80/file_list',
        },
      ];
    },
  };