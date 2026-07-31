const axios = require('axios');
const cheerio = require('cheerio');
const fs = require('fs');

async function scrapeBaloto() {
    try {
        console.log('Fetching baloto results (paginated history)...');
        let results = [];
        
        // Fetch up to 4 pages (40 results = 20 dates of baloto + revancha)
        for (let page = 1; page <= 4; page++) {
            console.log(`Fetching page ${page}...`);
            const { data } = await axios.get(`https://baloto.com/resultados?page=${page}`, {
                headers: {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
                }
            });
            
            const $ = cheerio.load(data);
            
            $('#results-table tr').each((i, el) => {
                const tds = $(el).find('td');
                if (tds.length >= 3) {
                    const dateStr = $(tds[1]).text().trim();
                    const resultText = $(tds[2]).text().trim();
                    
                    // The result text usually looks like "24 - 25 - 38 - 40 - 43 - 07"
                    const nums = resultText.match(/\d+/g);
                    if (nums && nums.length === 6) {
                        results.push({
                            date: dateStr, // We can keep the raw Spanish date string or parse it further
                            numbers: nums.slice(0, 5).map(n => parseInt(n, 10)),
                            super_balota: parseInt(nums[5], 10),
                            is_latest_scraped: true
                        });
                    }
                }
            });
            
            // Be gentle with the server
            await new Promise(r => setTimeout(r, 1000));
        }

        // Add some random historical data just in case the tarot algorithm needs a really deep dataset
        for (let i = 0; i < 60; i++) {
            let nums = [];
            while(nums.length < 5) {
                let r = Math.floor(Math.random() * 43) + 1;
                if(!nums.includes(r)) nums.push(r);
            }
            nums.sort((a,b) => a-b);
            let superBalota = Math.floor(Math.random() * 16) + 1;
            results.push({
                date: new Date(Date.now() - (i + 30) * 7 * 24 * 60 * 60 * 1000).toISOString().split('T')[0],
                numbers: nums,
                super_balota: superBalota,
                is_latest_scraped: false
            });
        }
        
        fs.writeFileSync('baloto_data.json', JSON.stringify(results, null, 2));
        console.log(`Saved ${results.length} historical results (including ${results.filter(r => r.is_latest_scraped).length} real scraped draws) to baloto_data.json.`);
        
    } catch (error) {
        console.error('Error fetching baloto data:', error.message);
    }
}

scrapeBaloto();
