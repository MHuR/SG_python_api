This python3 script can be used to view stock information using the yfinance API.

The script has following dependencies (The modules can be installed using pip)
	yfinance
	pymongo

User Interface
	-At application startup Enter the number of stocks to be track.
	-Enter the ticker for each stock (Please specify a valid ticker).
	-View the stocks information via two available API's
		-To view all stocks in the database enter 1
		-To view a specific stock enter 2

Details:
The application uses the yfinance public API to get the stock information 
using the ticker. The stock informtion is stored in the stocks collection
of test database in MongoDB. The user can query database to get the stock
information. The script uses the multiprocessing module to spawn a new process
which updates the stock information every 30 seconds in the background.