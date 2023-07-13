import { execa } from 'execa';

// Number of files to build at a time
const batchSize = 10;

// Function to build a batch of files
async function buildBatch(files) {
  try {
    const args = ['build'];
    args.push(...files);

    await execa('npm run vitepress', args, { stdio: 'inherit' });
  } catch (error) {
    console.error(error);
    process.exit(1);
  }
}

// Main function to execute the partial build
async function buildPartial() {
  // List of all files to build
  const allFiles = [
    'file1.md',
    'file2.md',
    // Add more files here
  ];

  // Split the files into batches
  const batches = [];
  for (let i = 0; i < allFiles.length; i += batchSize) {
    batches.push(allFiles.slice(i, i + batchSize));
  }

  // Build each batch of files
  for (const batch of batches) {
    await buildBatch(batch);
  }
}

buildPartial();
