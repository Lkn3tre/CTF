import { PrismaClient } from '@prisma/client';
const prisma = new PrismaClient();
async function main() {
  const ASSET_URL = '/';
  const newshop = await prisma.shop.createMany({
    data: [
      {
        name: 'Some buds for you',
        price: 69,
        image: `${ASSET_URL}buds.jpeg`,
        Content:
          'Premium buds from the best growers in the world on their way to you!',
      },
      {
        name: 'Acid',
        price: 200,
        image: `${ASSET_URL}acidy.jpeg`,
        Content: 'Acid for our trippy friends!',
      },
      {
        name: 'Shrooms',
        price: 500,
        image: `${ASSET_URL}shroomy.jpg`,
        Content: 'Shrooms for our trippy friends!',
      },
      {
        name: 'Suspicious Stew',
        price: 1000,
        image: `${ASSET_URL}suspicious.webp`,
      },
      {
        name: 'Oxycodone',
        price: 100,
        image: `${ASSET_URL}oxy.png`,
        Content: 'Oxycodone for our crackheads!',
      },
      {
        name: 'Roids for our gym bros',
        price: 500,
        image:
          'https://imgnew.outlookindia.com/uploadimage/library/16_9/16_9_5/IMAGE_1667544581.jpg',
        Content: 'Trenbolone to get you jacked! (and a small pp)',
      },
      {
        name: 'Flag',
        price: 133742,
        image: `https://preview.free3d.com/img/2019/02/2169732366744946373/lydexpmd.jpg`,
        Content: 'Flag for our friends!: AKASEC{TESTFLAG}',
      },
    ],
    skipDuplicates: true,
  });
}
main()
  .then(async () => {
    await prisma.$disconnect();
  })
  .catch(async (e) => {
    console.error(e);
    await prisma.$disconnect();
    process.exit(1);
  });
