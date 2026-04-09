# Notes (fill this)


## OTLP vs OLAP
  *  OTLP is Online Transaction System that manages the transactional data, such data include sales transaction, online order, inventory update customer support interaction etc.
  *  It handles thousands of users performing transaction simaltenously.
  *  OTLP ensure instant update to the system with each transactions.
  *  OTLP ensure quick operation like adding, updating, or deleting of record

  * Whereas OLAP is Online Analytical Processing is the type of system that focus on analyzing large dataset, helping team to uncover the pattern, trend and insight for strategic decision making.
  * OLAP utlize a special data design known as OLAP Cube which organize data in multi dimensional array for more straight forward slicing.

## ETL vs ELT
  * ETL stands of Extract Transform Load the main difference between the ETL and ELT is the order in which they are performed.
  * Like in Data warehouses we use ETL becuase it uses Schema on Write like we have to first create the schema of the table before loading it so we have to perform the transformation before loading it into the data      warehouse.
  * Where as ELT is performed on Data Lakehouse which uses Schema on Read like we don't have to decide the schema before loading it into the data lakehouse we first load the data into its native format and perform the transformation when we query it.

## Batch vs Streaming 
  * Batch and Streaming are both the proccessing technique but the core difference between them is how they handle the passage of time.
  * Batch processing group the data and handle over the time interval.
  * Whereas the Streaming continously handle the data.
  * Batch processing is helpful where time senstive data is not required.
  * Streaming is useful where the handling continous flow of data required like network data for Anomaly or Intrusion detection.


## Medallion Architecture 
  * It is the data design patter used to logically organize dtaa in data lakehouse and its main goal is incrementally and progressivley imporve structure and quality of data as it flow through each layer.
  * It mainly has 3 layer Bronze, Silver and Gold

    # Bronze
      * First stage in the Medallion Architecture.
      * It contain all the raw data in its native format.
      * It is the landing zone for raw data.

    # Silver
      * The second stage in Medallion Architecture.
      * Where all the filtered cleaned and augmented data is stored.
      * In this stage we define the schema or enforce the schema.
      * Schema can be evlove as and when needed.
      * All the tranformation techniques like data cleaning and validation, deduplication are done.

    # Gold
      * This the last stage of the this architecture where all the bussiness level data is stored.
      * In this stage there is continous updated, cleaned data to the downstream user and app.
      * This data can be used in Bussiness Intelligence and Machine Learning.

   ## Why raw data should not be queried directly?
     * Raw data should not be quired directly because there are many risk while quering the raw data.
     * Raw data is not always not sturctured like different date format, missing values or duplicate value.
     * It also increase the query time if that data is not stuctured.
       
      
