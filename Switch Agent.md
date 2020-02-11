CTP-SWITCH-AGENT-1
===

### AGENTS

Act as listeners for external enitites and react to changes

AgentRunner

    class agent(AgentRunner)
    
passes methods to agents

    self.conf = {**common, **agent}
    --> configParser = configparser.ConfigParser().read("agents.ini")
        common = dict(self.configParser.items('common'))
        agent = dict(self.configParser.items(agent_name))
        
    def run(self):
        self.execute_agent()
    --> if inherreted class has no execute_agent() method, it will default to using 
        AgentRunners method which just fails
        
agents.ini -> current address of test dev zixi box
        
    zixi_protocol = https
    zixi_address = 52.16.209.103
    zixi_port = 4444
    
ZixiClient()  -> requests session builder from confs