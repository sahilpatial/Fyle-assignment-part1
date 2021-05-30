# Fyle-assignment-part1
API usage
1) Autocomplete API Autocomplete API to return possible matches based on the branch name ordered by IFSC code (ascending order) with limit and offset.

Endpoint: /api/branches/autocomplete?q=<>

Example: /api/branches/autocomplete?q=RTGS&limit=3&offset=0

https://fyle-part1-api.herokuapp.com/api/branches/autocomplete?q=RTGS&limit=3&offset=0

API Response
{"branches":[{"address":"ABHYUDAYA BANK BLDG., B.NO.71, NEHRU NAGAR, KURLA (E), MUMBAI-400024","bank_id":60,"bank_name":"ABHYUDAYA COOPERATIVE BANK LIMITED","branch":"RTGS-HO","city":"MUMBAI","district":"GREATER MUMBAI","ifsc":"ABHY0065001","state":"MAHARASHTRA"},{"address":"414 EMPIRE COMPLEX, SENAPATI BAPAT MARG LOWER PAREL WEST MUMBAI 400013","bank_id":110,"bank_name":"THE ROYAL BANK OF SCOTLAND N V","branch":"RTGS-HO","city":"MUMBAI","district":"GREATER BOMBAY","ifsc":"ABNA0000001","state":"MAHARASHTRA"},{"address":"75, REHMAT MANZIL, V. N. ROAD, CURCHGATE, MUMBAI - 400020","bank_id":143,"bank_name":"ABU DHABI COMMERCIAL BANK","branch":"RTGS-HO","city":"MUMBAI","district":"MUMBAI CITY","ifsc":"ADCB0000001","state":"MAHARASHTRA"}]}

2) Search API

Search API to return possible matches across all columns and all rows, ordered by IFSC code (ascending order) with limit and offset.

https://fyle-part1-api.herokuapp.com/api/branches?q=Bangalore&limit=4&offset=0
Endpoint: /api/branches?q=<>
Example: /api/branches?q=Bangalore&limit=4&offset=0
API Response
{"branches":[{"address":"PRESTIGE TOWERS', GROUND FLOOR, 99 & 100, RESIDENCY ROAD, BANGALORE 560 025.","bank_id":110,"bank_name":"THE ROYAL BANK OF SCOTLAND N V","branch":"BANGALORE","city":"BANGALORE","district":"BANGALORE URBAN","ifsc":"ABNA0100318","state":"KARNATAKA"},{"address":"CITI CENTRE, 28, CHURCH STREET, OFF M. G. ROAD BANGALORE 560001","bank_id":143,"bank_name":"ABU DHABI COMMERCIAL BANK","branch":"BANGALORE","city":"BANGALORE","district":"BANGALORE URBAN","ifsc":"ADCB0000002","state":"KARNATAKA"},{"address":"NO. 2, FKCCI BUILDING , K G ROAD , BANGALORE","bank_id":11,"bank_name":"ALLAHABAD BANK","branch":"K. G. ROAD","city":"BANGALORE","district":"BANGALORE URBAN","ifsc":"ALLA0210217","state":"KARNATAKA"},{"address":"121, RM COMPLEX, DR.D.V.GUNDAPPA ROAD, BASAVANGUDI, BANGALORE - 560004","bank_id":11,"bank_name":"ALLAHABAD BANK","branch":"BANGALORE BASAVANGUDI","city":"BANGALORE","district":"BANGALORE URBAN","ifsc":"ALLA0210326","state":"KARNATAKA"}]}
