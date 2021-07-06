str1 = "On branch master\n\
Your branch is up to date with 'origin/master'.\n\
\n\
Changes not staged for commit:\n\
  (use \"git add <file>...\" to update what will be committed)\n\
  (use \"git checkout -- <file>...\" to discard changes in working directory)\n\
\n\
	modified:   alive_progress/styles/exhibit.py\n\
\n\
Untracked files:\n\
  (use \"git add <file>...\" to include in what will be committed)\n\
\n\
	horizontal_show.py\n\
	s.py\n\
	try.py\n\
	vertial_show_1_block.py\n\
	vertial_show_2_block.py\n\
	vertial_show_3_block.py\n\
	vertial_show_block.py\n\
	vertial_show_block.py.7z\n\
	vertial_show_block.py.bak\n\
\n\
no changes added to commit (use \"git add\" and/or \"git commit -a\")"

str2 = "*                                    (HEAD -> master) | 5e30666010 | 2021-06-05 16:48:59 -0700 | dhyun@apple.com        | [SPARK-35656][BUILD] Upgrade SBT to 1.5.3\n\
*                                                     | 6f8c62047c | 2021-06-05 14:25:33 -0500 | srowen@gmail.com       | [SPARK-35558] Optimizes for multi-quantile retrieval\n\
*                                                     | 510bde460a | 2021-06-05 17:45:44 +0800 | gengliang@apache.org   | [SPARK-35655][BUILD] Upgrade HtmlUnit and its related artifacts to 2.50\n\
*                                                     | 7bc364beed | 2021-06-05 14:49:16 +0800 | gengliang@apache.org   | [SPARK-35621][SQL] Add rule id pruning to the TypeCoercion rule\n\
*                                                     | b5678bee1e | 2021-06-05 12:44:16 +0900 | gurwls223@apache.org   | [SPARK-35446] Override getJDBCType in MySQLDialect to map FloatType to FLOAT\n\
*                                                     | f2c0a049a6 | 2021-06-05 12:40:39 +0900 | gurwls223@apache.org   | [SPARK-35643][PYTHON] Fix ambiguous reference in functions.py column()\n\
*                                                     | 497c80a1ad | 2021-06-04 06:59:49 -0700 | dhyun@apple.com        | [SPARK-32975][K8S] Add config for driver readiness timeout before executors start\n\
*                                                     | dc3317fdf9 | 2021-06-04 13:32:56 +0000 | wenchen@databricks.com | [SPARK-21957][SQL][FOLLOWUP] Support CURRENT_USER without tailing parentheses\n\
*                                                     | 6ce5f2491c | 2021-06-04 13:29:36 +0000 | wenchen@databricks.com | [SPARK-35568][SQL] Add the BroadcastExchange afte..OperationException when enabling both AQE and DPP\n\
*                                                     | c7fb0e18be | 2021-06-04 15:52:21 +0800 | gengliang@apache.org   | [SPARK-35629][SQL] Use better exception type if database doesn't exist on `drop database`\n\
*                                                     | 53a758b51b | 2021-06-04 15:44:32 +0900 | gurwls223@apache.org   | [SPARK-35636][SQL] Lambda keys should not be referenced outside of the lambda function\n\
*                                                     | 807b4006ca | 2021-06-04 15:02:29 +0900 | gurwls223@apache.org   | [SPARK-35648][PYTHON] Refine and add dependencies needed for dev in dev/requirement.txt\n\
*                                                     | 7c32415669 | 2021-06-04 14:08:13 +0900 | gurwls223@apache.org   | [SPARK-35523] Fix the default value in Data Source Options page\n\
*                                                     | 63ab38f917 | 2021-06-03 21:54:27 -0700 | dhyun@apple.com        | [SPARK-35396][CORE][FOLLOWUP] Free memory entry immediately\n\
*                                                     | 221553c204 | 2021-06-04 12:52:52 +0900 | gurwls223@apache.org   | [SPARK-35642][INFRA] Split pyspark-pandas tests to rebalance the test duration\n\
*                                                     | 3d158f9c91 | 2021-06-04 11:11:09 +0900 | gurwls223@apache.org   | [SPARK-35587][PYTHON][DOCS] Initial porting of Koalas documentation\n\
*                                                     | 745bd090f7 | 2021-06-04 10:28:12 +0900 | gurwls223@apache.org   | [SPARK-35589][CORE][TESTS][FOLLOWUP] Remove the duplicated test coverage\n\
*                                                     | 7eeb07d0f9 | 2021-06-03 14:24:53 -0700 | dhyun@apple.com        | [SPARK-35606][PYTHON][INFRA] List Python 3.9 installed libraries in build_and_test workflow\n\
*                                                     | 878527d9fa | 2021-06-03 14:07:26 -0700 | dhyun@apple.com        | [SPARK-35612][SQL] Support LZ4 compression in ORC data source\n\
*                                                     | 0342dcb628 | 2021-06-03 09:16:47 -0700 | viirya@gmail.com       | [SPARK-35580][SQL] Implement canonicalized method for HigherOrderFunction\n\
*                                                     | 4f0db872a0 | 2021-06-03 10:41:11 -0500 | mridulatgmail.com      | [SPARK-35416][K8S][FOLLOWUP] Use Set instead of ArrayBuffer\n\
*                                                     | cfde117c6f | 2021-06-03 14:45:17 +0000 | wenchen@databricks.com | [SPARK-35316][SQL] UnwrapCastInBinaryComparison support In/InSet predicate\n\
*                                                     | c532f8260e | 2021-06-03 21:52:41 +0900 | sarutak@oss.nttdata.com | [SPARK-35609][BUILD] Add style rules to prohibit ..a's API which is incompatible with newer versions\n\
*                                                     | 2658bc590f | 2021-06-03 13:52:46 +0900 | gurwls223@apache.org   | [SPARK-35081][DOCS] Add Data Source Option links to missing documents\n\
*                                                     | 4a549f2de2 | 2021-06-03 13:52:04 +0900 | gurwls223@apache.org   | [SPARK-35574][BUILD] Add a compile arg to turn co..edure syntax` to compilation errors in Scala 2.13\n\
*                                                     | e0bccc1831 | 2021-06-03 12:49:10 +0900 | gurwls223@apache.org   | [SPARK-35528][DOCS] Add more options at Data Source Options pages\n\
*                                                     | d478cff8bb | 2021-06-03 12:48:30 +0900 | gurwls223@apache.org   | [SPARK-35620][BUILD][PYTHON] Remove documentation build in Python linter\n\
*                                                     | b9e53f8937 | 2021-06-03 11:15:50 +0800 | yi.wu@databricks.com   | [SPARK-35011][CORE] Avoid Block Manager registrations when StopExecutor msg is in-flight\n\
*                                                     | 2550490c09 | 2021-06-02 18:30:38 -0700 | dhyun@apple.com        | [SPARK-35617][INFRA] Update GitHub Action docker image to 20210602\n\
*                                                     | 806edf8f44 | 2021-06-02 09:34:28 -0700 | dhyun@apple.com        | [SPARK-35610][CORE] Fix the memory leak introduced by the Executor's stop shutdown hook\n\
*                                                     | 8041aed296 | 2021-06-02 14:14:37 +0000 | wenchen@databricks.com | [SPARK-34808][SQL][FOLLOWUP] Remove canPlanAsBroadcastHashJoin check in EliminateOuterJoin\n\
*                                                     | 9f7cdb89f7 | 2021-06-02 13:06:55 +0000 | wenchen@databricks.com | [SPARK-35059][SQL] Group exception messages in hive/execution\n\
*                                                     | 345d35ed1a | 2021-06-02 13:04:40 +0000 | wenchen@databricks.com | [SPARK-21957][SQL] Support current_user function\n\
*                                                     | daf9d198dc | 2021-06-02 07:49:56 +0000 | wenchen@databricks.com | [SPARK-35585][SQL] Support propagate empty relation through project/filter\n\
*                                                     | 54e9999d39 | 2021-06-02 14:01:34 +0800 | ltnwgl@gmail.com       | [SPARK-35604][SQL] Fix condition check for FULL OUTER sort merge join\n\
*                                                     | 48252bac95 | 2021-06-02 14:21:16 +0900 | gurwls223@apache.org   | [SPARK-35583][DOCS] Move JDBC data source options from Python and Scala into a single page\n\
*                                                     | 3f6322f9aa | 2021-06-02 11:46:33 +0800 | gengliang@apache.org   | [SPARK-35077][SQL] Migrate to transformWithPruning for leftover optimizer rules\n\
*                                                     | c2de0a64e9 | 2021-06-02 10:47:45 +0800 | ruifengz@foxmail.com   | [SPARK-35100][ML] Refactor AFT - support virtual centering\n\
*                                                     | dbf0b50757 | 2021-06-01 19:13:12 -0700 | viirya@gmail.com       | [SPARK-35560][SQL] Remove redundant subexpression evaluation in nested subexpressions\n\
*                                                     | 9d0d4edb43 | 2021-06-02 10:05:29 +0800 | gengliang@apache.org   | [SPARK-35595][TESTS] Support multiple loggers in testing method withLogAppender\n\
*                                                     | 0ad5ae54b2 | 2021-06-02 10:39:24 +0900 | gurwls223@apache.org   | [SPARK-35539][PYTHON] Restore to_koalas to keep the backward compatibility\n\
*                                                     | 6a277bb7c6 | 2021-06-02 10:36:21 +0900 | gurwls223@apache.org   | [SPARK-35600][TESTS] Move Set command related test cases to SetCommandSuite\n\
*                                                     | 35cfabcf5c | 2021-06-01 14:23:24 -0700 | dhyun@apple.com        | [SPARK-35589][CORE] BlockManagerMasterEndpoint sh..ot ignore index-only shuffle file during updating\n\
*                                                     | 0ac5c16177 | 2021-06-01 10:57:12 -0700 | ueshin@databricks.com  | [SPARK-35314][PYTHON] Support arithmetic operations against bool IndexOpsMixin\n\
*                                                     | a127d91292 | 2021-06-02 01:02:41 +0800 | yao@apache.org         | [SPARK-35402][WEBUI] Increase the max thread pool size of jetty server in HistoryServer UI\n\
*                                                     | 08e6f633b5 | 2021-06-01 22:44:48 +0900 | yamamuro@apache.org    | [SPARK-35577][TESTS] Allow to log container output for docker integration tests\n\
*                                                     | a59063d544 | 2021-06-01 15:29:05 +0300 | max.gekk@gmail.com     | [SPARK-35581][SQL] Support special datetime values in typed literals only\n\
*                                                     | b7dd4b37e5 | 2021-06-01 19:00:13 +0900 | sarutak@oss.nttdata.com | [SPARK-35516][WEBUI] Storage UI tab Storage Level tool tip correction\n\
*                                                     | d773373074 | 2021-06-01 00:45:58 -0700 | dhyun@apple.com        | [SPARK-35584][CORE][TESTS] Increase the timeout in FallbackStorageSuite\n\
*                                                     | e04883880f | 2021-06-01 00:40:02 -0700 | dhyun@apple.com        | [SPARK-35586][K8S][TESTS] Set a default value for..rkTgz in pom.xml for Kubernetes integration tests\n\
*                                                     | fe09def323 | 2021-06-01 15:24:04 +0900 | gurwls223@apache.org   | [SPARK-35582][PYTHON][DOCS] Remove # noqa in Python API documents\n\
*                                                     | 1dd0ca23f6 | 2021-06-01 11:39:42 +0800 | gengliang@apache.org   | [SPARK-35544][SQL] Add tree pattern pruning to Analyzer rules\n\
*                                                     | 73d4f67145 | 2021-06-01 10:58:49 +0900 | gurwls223@apache.org   | [SPARK-35433][DOCS] Move CSV data source options from Python and Scala into a single page\n\
*                                                     | bb2a0747d2 | 2021-06-01 10:51:05 +0900 | gurwls223@apache.org   | [SPARK-35578][SQL][TEST] Add a test case for a bug in janino\n\
*                                                     | 1ba1b70cfe | 2021-06-01 10:35:52 +0900 | gurwls223@apache.org   | [SPARK-35573][R][TESTS] Make SparkR tests pass with R 4.1+\n\
*                                                     | 7e2717333b | 2021-06-01 10:33:10 +0900 | gurwls223@apache.org   | [SPARK-35453][PYTHON] Move Koalas accessor to pandas_on_spark accessor\n\
*                                                     | 8e11f5f007 | 2021-05-31 14:50:18 -0700 | dhyun@apple.com        | [SPARK-35576][SQL] Redact the sensitive info in the result of Set command\n\
*                                                     | cd2ef9cb43 | 2021-06-01 00:55:29 +0800 | wenchen@databricks.com | [SPARK-35567][SQL] Fix: Explain cost is not showing statistics for all the nodes\n\
*                                                     | 1603775934 | 2021-05-31 22:15:26 +0800 | wenchen@databricks.com | [SPARK-35411][SQL][FOLLOWUP] Handle Currying Product while serializing TreeNode to JSON\n\
*                                                     | 14e12c64d3 | 2021-05-31 19:29:54 +0900 | gurwls223@apache.org   | [SPARK-35575][INFRA] Recover updating build status in GitHub Actions\n\
*                                                     | 6cd6c438f2 | 2021-05-31 18:14:15 +0800 | yumwang@ebay.com       | [SPARK-34808][SQL] Removes outer join if it only has DISTINCT on streamed side\n\
*                                                     | 8c69e9cd94 | 2021-05-31 02:43:58 -0700 | dhyun@apple.com        | [SPARK-35562][DOC] Fix docs about Kubernetes and Yarn\n\
*                                                     | 73ba4492b1 | 2021-05-31 16:45:56 +0900 | gurwls223@apache.org   | [SPARK-35566][SS] Fix StateStoreRestoreExec output rows\n\
*                                                     | c225196be0 | 2021-05-31 05:56:47 +0000 | dhyun@apple.com        | [SPARK-35507][INFRA] Add Python 3.9 in the docker image for GitHub Action\n\
*                                                     | 806da9d6fa | 2021-05-31 04:57:24 +0000 | wenchen@databricks.com | [SPARK-35545][SQL] Split SubqueryExpression's chi..n field into outer attributes and join conditions"

str3 = "Updating 5e30666010..4dabba8f76\n\
Checking out files: 100% (1105/1105), done.\n\
Fast-forward\n\
 .github/workflows/build_and_test.yml                                                                                                    |    12 +-\n\
 .gitignore                                                                                                                              |     8 +-\n\
 R/pkg/R/DataFrame.R                                                                                                                     |    19 +\n\
 R/pkg/R/SQLContext.R                                                                                                                    |    19 +\n\
 R/pkg/R/functions.R                                                                                                                     |     8 +\n\
 README.md                                                                                                                               |     1 +\n\
 binder/postBuild                                                                                                                        |     2 +-\n\
 build/sbt                                                                                                                               |     2 +-\n\
 common/kvstore/src/test/java/org/apache/spark/util/kvstore/DBIteratorSuite.java                                                         |     2 +-\n\
 common/kvstore/src/test/java/org/apache/spark/util/kvstore/IntKeyType.java                                                              |    47 +\n\
 common/kvstore/src/test/java/org/apache/spark/util/kvstore/LevelDBSuite.java                                                            |    27 -\n\
 common/network-common/src/main/java/org/apache/spark/network/client/BaseResponseCallback.java                                           |    31 +\n\
 common/network-common/src/main/java/org/apache/spark/network/client/MergedBlockMetaResponseCallback.java                                |    41 +\n\
 common/network-shuffle/src/test/java/org/apache/spark/network/shuffle/OneForOneBlockFetcherSuite.java                                   |    55 +-\n\
 common/network-shuffle/src/test/java/org/apache/spark/network/shuffle/protocol/FetchShuffleBlockChunksSuite.java                        |    42 +\n\
 common/network-shuffle/src/test/java/org/apache/spark/network/shuffle/protocol/FetchShuffleBlocksSuite.java                             |    42 +\n\
 common/sketch/src/main/java/org/apache/spark/util/sketch/BitArray.java                                                                  |    11 +\n\
 common/sketch/src/main/java/org/apache/spark/util/sketch/BloomFilter.java                                                               |    10 +\n\
 common/sketch/src/main/java/org/apache/spark/util/sketch/BloomFilterImpl.java                                                           |    20 +-\n\
 common/sketch/src/test/scala/org/apache/spark/util/sketch/BloomFilterSuite.scala                                                        |    30 +\n\
 core/benchmarks/ZStandardBenchmark-jdk11-results.txt                                                                                    |    32 +-\n\
 core/src/test/resources/META-INF/services/org.apache.spark.scheduler.ExternalClusterManager                                             |     1 +\n\
 core/src/test/scala/org/apache/spark/util/UtilsSuite.scala                                                                              |    12 +-\n\
 dev/create-release/release-build.sh                                                                                                     |     2 +-\n\
 dev/create-release/spark-rm/Dockerfile                                                                                                  |     2 +-\n\
 dev/deps/spark-deps-hadoop-2.7-hive-2.3                                                                                                 |    70 +-\n\
 dev/deps/spark-deps-hadoop-3.2-hive-2.3                                                                                                 |    78 +-\n\
 dev/lint-python                                                                                                                         |    32 +\n\
 dev/reformat-python                                                                                                                     |    32 +\n\
 dev/requirements.txt                                                                                                                    |     3 +\n\
 dev/sparktestsupport/modules.py                                                                                                         |     4 +\n\
 dev/tox.ini                                                                                                                             |     4 +-\n\
 docs/building-spark.md                                                                                                                  |    10 +-\n\
 docs/cluster-overview.md                                                                                                                |     3 -\n\
 docs/configuration.md                                                                                                                   |     2 +-\n\
 docs/job-scheduling.md                                                                                                                  |     6 +-\n\
 docs/sql-data-sources-hive-tables.md                                                                                                    |     8 +-\n\
 docs/sql-migration-guide.md                                                                                                             |     4 +-\n\
 docs/sql-performance-tuning.md                                                                                                          |     3 +-\n\
 docs/sql-ref-ansi-compliance.md                                                                                                         |     4 +-\n\
 docs/sql-ref-datatypes.md                                                                                                               |     2 +-\n\
 docs/structured-streaming-kafka-integration.md                                                                                          |    29 +-\n\
 external/avro/benchmarks/AvroReadBenchmark-results.txt                                                                                  |   115 +-\n\
 external/avro/benchmarks/AvroWriteBenchmark-results.txt                                                                                 |    20 +-\n\
 external/avro/pom.xml                                                                                                                   |    11 +\n\
 external/avro/src/main/scala/org/apache/spark/sql/avro/AvroDeserializer.scala                                                           |     3 +-\n\
 external/avro/src/main/scala/org/apache/spark/sql/avro/AvroSerializer.scala                                                             |     4 +-\n\
 external/avro/src/main/scala/org/apache/spark/sql/avro/AvroUtils.scala                                                                  |    47 +-\n\
 external/avro/src/test/scala/org/apache/spark/sql/avro/AvroSchemaHelperSuite.scala                                                      |    67 +\n\
 external/avro/src/test/scala/org/apache/spark/sql/execution/benchmark/AvroWriteBenchmark.scala                                          |    32 +\n\
 external/kafka-0-10-sql/pom.xml                                                                                                         |    12 +-\n\
 external/kafka-0-10-token-provider/src/main/scala/org/apache/spark/kafka010/KafkaDelegationTokenProvider.scala                          |     5 +-\n\
 graphx/src/main/scala/org/apache/spark/graphx/util/GraphGenerators.scala                                                                |    13 +-\n\
 mllib-local/src/main/scala/org/apache/spark/ml/impl/Utils.scala                                                                         |    43 +\n\
 mllib-local/src/main/scala/org/apache/spark/ml/linalg/BLAS.scala                                                                        |    64 +-\n\
 mllib/src/main/scala/org/apache/spark/ml/classification/LogisticRegression.scala                                                        |    29 +-\n\
 mllib/src/main/scala/org/apache/spark/ml/classification/NaiveBayes.scala                                                                |    15 +-\n\
 mllib/src/main/scala/org/apache/spark/ml/optim/aggregator/AFTBlockAggregator.scala                                                      |    35 +-\n\
 mllib/src/main/scala/org/apache/spark/ml/optim/aggregator/BinaryLogisticBlockAggregator.scala                                           |    34 +-\n\
 mllib/src/main/scala/org/apache/spark/ml/optim/aggregator/HingeBlockAggregator.scala                                                    |    34 +-\n\
 mllib/src/main/scala/org/apache/spark/ml/optim/aggregator/HuberAggregator.scala                                                         |   250 ---\n\
 mllib/src/main/scala/org/apache/spark/ml/optim/aggregator/HuberBlockAggregator.scala                                                    |   150 ++\n\
 mllib/src/main/scala/org/apache/spark/ml/optim/aggregator/LeastSquaresAggregator.scala                                                  |   314 ---\n\
 mllib/src/main/scala/org/apache/spark/ml/optim/aggregator/LeastSquaresBlockAggregator.scala                                             |   124 ++\n\
 mllib/src/main/scala/org/apache/spark/ml/optim/aggregator/MultinomialLogisticBlockAggregator.scala                                      |    80 +-\n\
 mllib/src/test/scala/org/apache/spark/ml/optim/aggregator/{LeastSquaresAggregatorSuite.scala => LeastSquaresBlockAggregatorSuite.scala} |   135 +-\n\
 mllib/src/test/scala/org/apache/spark/ml/recommendation/ALSSuite.scala                                                                  |    15 +-\n\
 pom.xml                                                                                                                                 |    42 +-\n\
 python/docs/source/conf.py                                                                                                              |    15 +-\n\
 python/docs/source/development/contributing.rst                                                                                         |   123 +-\n\
 python/docs/source/getting_started/ps_10mins.ipynb                                                                                      | 14471 ---------------------------------------------------------------------------------------------------------------------------\n\
 python/docs/source/getting_started/ps_install.rst                                                                                       |   145 --\n\
 python/docs/source/getting_started/ps_videos_blogs.rst                                                                                  |   130 --\n\
 python/docs/source/getting_started/{quickstart.ipynb => quickstart_df.ipynb}                                                            |    10 +-\n\
 python/docs/source/getting_started/quickstart_ps.ipynb                                                                                  | 14489 ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n\
 python/docs/source/index.rst                                                                                                            |     5 +-\n\
 python/docs/source/index.rst                                                                                                            |     5 +-\n\
 python/docs/source/migration_guide/pyspark_3.1_to_3.2.rst                                                                               |     6 +\n\
 python/docs/source/reference/index.rst                                                                                                  |    16 +-\n\
 python/docs/source/reference/{ps_extensions.rst => pyspark.pandas/extensions.rst}                                                       |     6 +-\n\
 python/docs/source/reference/{ps_frame.rst => pyspark.pandas/frame.rst}                                                                 |     6 +-\n\
 python/docs/source/reference/{ps_general_functions.rst => pyspark.pandas/general_functions.rst}                                         |     0\n\
 python/docs/source/reference/{ps_groupby.rst => pyspark.pandas/groupby.rst}                                                             |     0\n\
 python/docs/source/reference/pyspark.pandas/index.rst                                                                                   |    36 +\n\
 python/docs/source/reference/{ps_indexing.rst => pyspark.pandas/indexing.rst}                                                           |     0\n\
 python/docs/source/user_guide/index.rst                                                                                                 |    16 +-\n\
 python/docs/source/user_guide/{ps_best_practices.rst => pandas_on_spark/best_practices.rst}                                             |   138 +-\n\
 python/pyspark/pandas/extensions.py                                                                                                     |     4 +-\n\
 python/pyspark/pandas/tests/data_type_ops/test_base.py                                                                                  |    98 +\n\
 python/pyspark/pandas/tests/data_type_ops/test_binary_ops.py                                                                            |    48 +-\n\
 python/pyspark/pandas/tests/data_type_ops/test_boolean_ops.py                                                                           |   381 +++-\n\
 python/pyspark/pandas/tests/data_type_ops/test_categorical_ops.py                                                                       |    54 +-\n\
 python/pyspark/pandas/tests/data_type_ops/test_complex_ops.py                                                                           |    67 +-\n\
 resource-managers/kubernetes/core/src/main/scala/org/apache/spark/deploy/k8s/submit/KubernetesClientApplication.scala                   |     9 +-\n\
 resource-managers/kubernetes/core/src/main/scala/org/apache/spark/scheduler/cluster/k8s/ExecutorPodsAllocator.scala                     |    25 +-\n\
 resource-managers/kubernetes/core/src/main/scala/org/apache/spark/shuffle/KubernetesLocalDiskShuffleDataIO.scala                        |    37 +\n\
 resource-managers/kubernetes/core/src/main/scala/org/apache/spark/shuffle/KubernetesLocalDiskShuffleExecutorComponents.scala            |   102 +\n\
 resource-managers/kubernetes/core/src/test/scala/org/apache/spark/scheduler/cluster/k8s/ExecutorPodsAllocatorSuite.scala                |    20 +-\n\
 resource-managers/kubernetes/core/src/test/scala/org/apache/spark/shuffle/KubernetesLocalDiskShuffleDataIOSuite.scala                   |   222 ++\n\
 resource-managers/yarn/pom.xml                                                                                                          |    16 +\n\
 resource-managers/yarn/src/main/scala/org/apache/spark/deploy/yarn/Client.scala                                                         |     8 +-\n\
 resource-managers/yarn/src/test/scala/org/apache/spark/network/yarn/YarnShuffleServiceMetricsSuite.scala                                |     3 +-\n\
 resource-managers/yarn/src/test/scala/org/apache/spark/network/yarn/YarnShuffleServiceSuite.scala                                       |     3 +-\n\
 sql/catalyst/src/main/antlr4/org/apache/spark/sql/catalyst/parser/SqlBase.g4                                                            |    22 +-\n\
 sql/catalyst/src/main/java/org/apache/spark/sql/catalyst/expressions/SpecializedGettersReader.java                                      |     3 +\n\
 sql/catalyst/src/main/java/org/apache/spark/sql/catalyst/expressions/UnsafeRow.java                                                     |    12 +-\n\
 sql/catalyst/src/main/java/org/apache/spark/sql/connector/catalog/functions/ScalarFunction.java                                         |     3 +\n\
 sql/catalyst/src/main/java/org/apache/spark/sql/connector/read/streaming/CompositeReadLimit.java                                        |    59 +\n\
 sql/catalyst/src/main/java/org/apache/spark/sql/connector/read/streaming/ReadLimit.java                                                 |     8 +\n\
 sql/catalyst/src/main/java/org/apache/spark/sql/connector/read/streaming/ReadMinRows.java                                               |    65 +\n\
 sql/catalyst/src/main/java/org/apache/spark/sql/types/DataTypes.java                                                                    |    43 +-\n\
 sql/catalyst/src/main/scala/org/apache/spark/sql/Encoders.scala                                                                         |     8 +\n\
 sql/catalyst/src/main/scala/org/apache/spark/sql/catalyst/CatalystTypeConverters.scala                                                  |    41 +-\n\
 sql/catalyst/src/main/scala/org/apache/spark/sql/catalyst/DeserializerBuildHelper.scala                                                 |     9 +\n\
 sql/catalyst/src/main/scala/org/apache/spark/sql/catalyst/InternalRow.scala                                                             |     8 +-\n\
 sql/catalyst/src/main/scala/org/apache/spark/sql/catalyst/plans/logical/hints.scala                                                     |     5 +-\n\
 sql/catalyst/src/main/scala/org/apache/spark/sql/catalyst/plans/logical/statsEstimation/BasicStatsPlanVisitor.scala                     |     9 +-\n\
 sql/catalyst/src/main/scala/org/apache/spark/sql/catalyst/plans/logical/statsEstimation/SizeInBytesOnlyStatsPlanVisitor.scala           |     6 +-\n\
 sql/catalyst/src/main/scala/org/apache/spark/sql/catalyst/trees/TreePatterns.scala                                                      |     3 +\n\
 sql/catalyst/src/main/scala/org/apache/spark/sql/catalyst/util/DateTimeFormatterHelper.scala                                            |     9 +-\n\
 sql/catalyst/src/main/scala/org/apache/spark/sql/catalyst/util/DateTimeUtils.scala                                                      |   145 +-\n\
 sql/catalyst/src/main/scala/org/apache/spark/sql/catalyst/util/IntervalUtils.scala                                                      |   173 +-\n\
 sql/catalyst/src/main/scala/org/apache/spark/sql/catalyst/util/TimestampFormatter.scala                                                 |    84 +-\n\
 sql/catalyst/src/main/scala/org/apache/spark/sql/catalyst/util/TypeUtils.scala                                                          |     5 +-\n\
 sql/catalyst/src/main/scala/org/apache/spark/sql/errors/QueryCompilationErrors.scala                                                    |    52 +-\n\
 sql/catalyst/src/main/scala/org/apache/spark/sql/errors/QueryExecutionErrors.scala                                                      |   182 +-\n\
 sql/catalyst/src/main/scala/org/apache/spark/sql/errors/QueryParsingErrors.scala                                                        |    16 +\n\
 sql/catalyst/src/main/scala/org/apache/spark/sql/internal/SQLConf.scala                                                                 |   110 +-\n\
 sql/catalyst/src/main/scala/org/apache/spark/sql/sources/filters.scala                                                                  |     5 +-\n\
 sql/catalyst/src/main/scala/org/apache/spark/sql/types/DataType.scala                                                                   |    17 +-\n\
 sql/catalyst/src/main/scala/org/apache/spark/sql/types/DayTimeIntervalType.scala                                                        |    57 +-\n\
 sql/catalyst/src/main/scala/org/apache/spark/sql/types/TimestampWithoutTZType.scala                                                     |    65 +\n\
 sql/catalyst/src/main/scala/org/apache/spark/sql/types/YearMonthIntervalType.scala                                                      |    53 +-\n\
 sql/catalyst/src/main/scala/org/apache/spark/sql/util/ArrowUtils.scala                                                                  |     8 +-\n\
 sql/catalyst/src/test/scala/org/apache/spark/sql/RandomDataGenerator.scala                                                              |    66 +-\n\
 sql/catalyst/src/test/scala/org/apache/spark/sql/RandomDataGeneratorSuite.scala                                                         |     3 +-\n\
 sql/catalyst/src/test/scala/org/apache/spark/sql/catalyst/CatalystTypeConvertersSuite.scala                                             |    66 +-\n\
 sql/catalyst/src/test/scala/org/apache/spark/sql/catalyst/analysis/AnalysisErrorSuite.scala                                             |    16 +\n\
 sql/catalyst/src/test/scala/org/apache/spark/sql/catalyst/analysis/AnalysisSuite.scala                                                  |     8 +-\n\
 sql/core/src/main/scala/org/apache/spark/sql/execution/streaming/state/SymmetricHashJoinStateManager.scala                              |    28 +-\n\
 sql/hive-thriftserver/pom.xml                                                                                                           |    11 +\n\
 sql/hive-thriftserver/src/main/scala/org/apache/spark/sql/hive/thriftserver/SparkExecuteStatementOperation.scala                        |     7 +-\n\
 sql/hive-thriftserver/src/main/scala/org/apache/spark/sql/hive/thriftserver/SparkGetColumnsOperation.scala                              |     5 +-\n\
 sql/hive-thriftserver/src/test/scala/org/apache/spark/sql/hive/thriftserver/SparkMetadataOperationSuite.scala                           |     8 +-\n\
 sql/hive/pom.xml                                                                                                                        |     4 -\n\
 sql/hive/src/main/scala/org/apache/spark/sql/hive/HiveInspectors.scala                                                                  |    20 +-\n\
 sql/hive/src/main/scala/org/apache/spark/sql/hive/HiveUtils.scala                                                                       |     2 +-\n\
 sql/hive/src/main/scala/org/apache/spark/sql/hive/client/HiveClientImpl.scala                                                           |    60 +-\n\
 sql/hive/src/main/scala/org/apache/spark/sql/hive/client/HiveShim.scala                                                                 |    29 +-\n\
 sql/hive/src/main/scala/org/apache/spark/sql/hive/client/IsolatedClientLoader.scala                                                     |    12 +-\n\
 sql/hive/src/main/scala/org/apache/spark/sql/hive/client/package.scala                                                                  |     2 +-\n\
 sql/hive/src/main/scala/org/apache/spark/sql/hive/execution/HiveTableScanExec.scala                                                     |     4 +-\n\
 sql/hive/src/main/scala/org/apache/spark/sql/hive/security/HiveDelegationTokenProvider.scala                                            |     2 +-\n\
 sql/hive/src/test/scala/org/apache/spark/sql/HiveCharVarcharTestSuite.scala                                                             |     9 +\n\
 sql/hive/src/test/scala/org/apache/spark/sql/hive/HiveExternalCatalogVersionsSuite.scala                                                |     2 +-\n\
 sql/hive/src/test/scala/org/apache/spark/sql/hive/execution/AggregationQuerySuite.scala                                                 |     3 +-\n\
 sql/hive/src/test/scala/org/apache/spark/sql/hive/execution/HiveSQLViewSuite.scala                                                      |    24 +-\n\
 sql/hive/src/test/scala/org/apache/spark/sql/hive/execution/HiveScriptTransformationSuite.scala                                         |    82 +-\n\
 sql/hive/src/test/scala/org/apache/spark/sql/hive/execution/HiveSerDeReadWriteSuite.scala                                               |    31 +\n\
 sql/hive/src/test/scala/org/apache/spark/sql/hive/execution/SQLMetricsSuite.scala                                                       |     6 +-\n\
 sql/hive/src/test/scala/org/apache/spark/sql/hive/test/TestHive.scala                                                                   |    14 +-\n\
 1087 files changed, 93966 insertions(+), 81746 deletions(-)\n\
 create mode 100644 common/kvstore/src/test/java/org/apache/spark/util/kvstore/IntKeyType.java\n\
 create mode 100644 common/network-common/src/main/java/org/apache/spark/network/client/BaseResponseCallback.java\n\
 create mode 100644 common/network-common/src/main/java/org/apache/spark/network/client/MergedBlockMetaResponseCallback.java\n\
 create mode 100644 common/network-common/src/main/java/org/apache/spark/network/protocol/MergedBlockMetaRequest.java\n\
 create mode 100644 common/network-common/src/main/java/org/apache/spark/network/protocol/MergedBlockMetaSuccess.java\n\
 create mode 100644 common/network-common/src/test/java/org/apache/spark/network/protocol/MergedBlockMetaSuccessSuite.java\n\
 create mode 100644 common/network-shuffle/src/main/java/org/apache/spark/network/shuffle/MergedBlocksMetaListener.java\n\
 create mode 100644 common/network-shuffle/src/main/java/org/apache/spark/network/shuffle/protocol/AbstractFetchShuffleBlocks.java\n\
 create mode 100644 common/network-shuffle/src/main/java/org/apache/spark/network/shuffle/protocol/FetchShuffleBlockChunks.java\n\
 create mode 100644 common/network-shuffle/src/test/java/org/apache/spark/network/shuffle/protocol/FetchShuffleBlockChunksSuite.java\n\
 create mode 100644 common/network-shuffle/src/test/java/org/apache/spark/network/shuffle/protocol/FetchShuffleBlocksSuite.java\n\
 create mode 100644 core/src/test/scala/org/apache/spark/LocalRootDirsTest.scala\n\
 create mode 100755 dev/reformat-python\n\
 create mode 100644 external/avro/src/test/scala/org/apache/spark/sql/avro/AvroSchemaHelperSuite.scala\n\
 delete mode 100644 mllib/src/main/scala/org/apache/spark/ml/optim/aggregator/HuberAggregator.scala\n\
 create mode 100644 mllib/src/main/scala/org/apache/spark/ml/optim/aggregator/HuberBlockAggregator.scala\n\
 delete mode 100644 mllib/src/main/scala/org/apache/spark/ml/optim/aggregator/LeastSquaresAggregator.scala\n\
 create mode 100644 mllib/src/main/scala/org/apache/spark/ml/optim/aggregator/LeastSquaresBlockAggregator.scala\n\
 delete mode 100644 mllib/src/test/scala/org/apache/spark/ml/optim/aggregator/HuberAggregatorSuite.scala\n\
 create mode 100644 mllib/src/test/scala/org/apache/spark/ml/optim/aggregator/HuberBlockAggregatorSuite.scala\n\
 rename mllib/src/test/scala/org/apache/spark/ml/optim/aggregator/{LeastSquaresAggregatorSuite.scala => LeastSquaresBlockAggregatorSuite.scala} (51%)\n\
 create mode 100644 resource-managers/kubernetes/core/src/main/scala/org/apache/spark/shuffle/KubernetesLocalDiskShuffleDataIO.scala\n\
 create mode 100644 resource-managers/kubernetes/core/src/main/scala/org/apache/spark/shuffle/KubernetesLocalDiskShuffleExecutorComponents.scala\n\
 create mode 100644 resource-managers/kubernetes/core/src/test/scala/org/apache/spark/shuffle/KubernetesLocalDiskShuffleDataIOSuite.scala\n\
 create mode 100644 sql/catalyst/src/main/java/org/apache/spark/sql/connector/read/streaming/CompositeReadLimit.java\n\
 create mode 100644 sql/catalyst/src/main/java/org/apache/spark/sql/connector/read/streaming/ReadMinRows.java\n\
 create mode 100644 sql/catalyst/src/main/scala/org/apache/spark/sql/types/TimestampWithoutTZType.scala\n\
 create mode 100644 sql/catalyst/src/test/scala/org/apache/spark/sql/catalyst/expressions/AnsiCastSuiteBase.scala\n\
 create mode 100644 sql/catalyst/src/test/scala/org/apache/spark/sql/catalyst/expressions/CastSuiteBase.scala\n\
 create mode 100644 sql/core/src/main/java/org/apache/spark/sql/execution/datasources/parquet/ParquetReadState.java\n\
 create mode 100644 sql/core/src/main/java/org/apache/spark/sql/execution/datasources/parquet/ParquetVectorUpdater.java\n\
 create mode 100644 sql/core/src/main/java/org/apache/spark/sql/execution/datasources/parquet/ParquetVectorUpdaterFactory.java\n\
 create mode 100644 sql/core/src/main/scala/org/apache/spark/sql/catalyst/plans/logical/CommandResult.scala\n\
 create mode 100644 sql/core/src/main/scala/org/apache/spark/sql/execution/CommandResultExec.scala\n\
 create mode 100644 sql/core/src/main/scala/org/apache/spark/sql/execution/aggregate/MergingSessionsExec.scala\n\
 create mode 100644 sql/core/src/main/scala/org/apache/spark/sql/execution/aggregate/MergingSessionsIterator.scala\n\
 create mode 100644 sql/core/src/main/scala/org/apache/spark/sql/execution/reuse/ReuseExchangeAndSubquery.scala\n\
 create mode 100644 sql/core/src/main/scala/org/apache/spark/sql/execution/streaming/state/SchemaHelper.scala\n\
 create mode 100644 sql/core/src/main/scala/org/apache/spark/sql/streaming/TestGroupState.scala\n\
 create mode 100644 sql/core/src/test/resources/sql-tests/inputs/join-lateral.sql\n\
 create mode 100644 sql/core/src/test/resources/sql-tests/results/join-lateral.sql.out\n\
 create mode 100644 sql/core/src/test/scala/org/apache/spark/sql/execution/ReuseExchangeAndSubquerySuite.scala\n\
 create mode 100644 sql/core/src/test/scala/org/apache/spark/sql/execution/columnar/RefCountedTestCachedBatchSerializerSuite.scala\n\
 create mode 100644 sql/core/src/test/scala/org/apache/spark/sql/execution/streaming/MergingSessionsIteratorSuite.scala"
