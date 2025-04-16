//
// SPDX-License-Identifier: LGPL-3.0-or-later
//

package in2c;

import inet.common.scenario.ScenarioManager;
import inet.networks.base.TsnNetworkBase;
import inet.node.contract.IEthernetNetworkNode;
import inet.node.ethernet.Eth100M;
import inet.node.ethernet.Eth1G;

network IN2C extends TsnNetworkBase
{
    @display("bgb=948,813");
    types:
        channel Eth100M extends inet.node.ethernet.Eth100M
        {
            @display("ls=,3");
        }

        channel Eth1G extends inet.node.ethernet.Eth1G
        {
            @display("ls=,4");
        }
    submodules:
		// Master clock for TSN time synchronization.
        masterClock: <> like IEthernetNetworkNode if typename != "" {
            @display("p=564,413;i=device/card");
        }

        Sensing_1: <> like IEthernetNetworkNode {
            @display("p=291,600");
        }
        Control_1: <> like IEthernetNetworkNode {
            @display("p=298,315");
        }
        RobotArm_1: <> like IEthernetNetworkNode {
            @display("p=291,400");
        }
        Inspection_1: <> like IEthernetNetworkNode {
            @display("p=386,600");
        }
        Actuating_1: <> like IEthernetNetworkNode {
            @display("p=291,491");
        }
        SwitchA_1: <> like IEthernetNetworkNode {
            @display("p=386,491");
        }
        SwitchB_1: <> like IEthernetNetworkNode {
            @display("p=386,400");
        }
        centralSwitch_1: <> like IEthernetNetworkNode {
            @display("p=477,491");
        }
        centralSwitch_2: <> like IEthernetNetworkNode {
            @display("p=652,491");
        }
        Actuating_2: <> like IEthernetNetworkNode {
            @display("p=835,491");
        }
        Control_2: <> like IEthernetNetworkNode {
            @display("p=835,315");
        }
        Inspection_2: <> like IEthernetNetworkNode {
            @display("p=740,600");
        }
        RobotArm_2: <> like IEthernetNetworkNode {
            @display("p=835,413");
        }
        Sensing_2: <> like IEthernetNetworkNode {
            @display("p=835,600");
        }
        SwitchA_2: <> like IEthernetNetworkNode {
            @display("p=740,491");
        }
        SwitchB_2: <> like IEthernetNetworkNode {
            @display("p=740,413");
        }
        centralSwitch_3: <> like IEthernetNetworkNode {
            @display("p=564,315");
        }
        qcSwitch_1: <> like IEthernetNetworkNode {
            @display("p=477,252");
        }
        qcSwitch_2: <> like IEthernetNetworkNode {
            @display("p=652,692");
        }
        Camera_1: <> like IEthernetNetworkNode {
            @display("p=386,252");
        }
        Camera_2: <> like IEthernetNetworkNode {
            @display("p=740,252");
        }
        HMI: <> like IEthernetNetworkNode {
            @display("p=477,692");
        }
        SCADA: <> like IEthernetNetworkNode {
            @display("p=740,692");
        }
        scenarioManager: ScenarioManager {
            @display("p=100,759;is=s");
        }
        MEC: <> like IEthernetNetworkNode {
            @display("p=664,315");
        }
    connections:

        // Core Switches Eth [0], [1]
        centralSwitch_1.ethg++ <--> Eth1G <--> centralSwitch_2.ethg++;
        centralSwitch_1.ethg++ <--> Eth1G <--> centralSwitch_3.ethg++;
        centralSwitch_2.ethg++ <--> Eth1G <--> centralSwitch_3.ethg++;


        // Cell 1. 

        //Eth[0] switches
        SwitchA_1.ethg++ <--> Eth1G <--> centralSwitch_1.ethg++;
        SwitchB_1.ethg++ <--> Eth1G <--> centralSwitch_1.ethg++;

        //Eth[1] switches
        SwitchB_1.ethg++ <--> Eth1G <--> SwitchA_1.ethg++;

        //Eth[0] units
        Sensing_1.ethg++ <--> Eth100M <--> SwitchA_1.ethg++;
        Actuating_1.ethg++ <--> Eth100M <--> SwitchA_1.ethg++;
        Inspection_1.ethg++ <--> Eth100M <--> SwitchA_1.ethg++;

        RobotArm_1.ethg++ <--> Eth100M <--> SwitchB_1.ethg++;
        Control_1.ethg++ <--> Eth100M <--> SwitchB_1.ethg++;


        // Cell 2. 
        //Eth[0] switches
        SwitchA_2.ethg++ <--> Eth1G <--> centralSwitch_2.ethg++;
        SwitchB_2.ethg++ <--> Eth1G <--> centralSwitch_2.ethg++;

        //Eth[1] switches
        SwitchB_2.ethg++ <--> Eth1G <--> SwitchA_2.ethg++;

        //Eth[0] units     
        Sensing_2.ethg++ <--> Eth100M <--> SwitchA_2.ethg++;
        Actuating_2.ethg++ <--> Eth100M <--> SwitchA_2.ethg++;
        Inspection_2.ethg++ <--> Eth100M <--> SwitchA_2.ethg++;

        RobotArm_2.ethg++ <--> Eth100M <--> SwitchB_2.ethg++;
        Control_2.ethg++ <--> Eth100M <--> SwitchB_2.ethg++;


		// Quality Control

        // Switches
        qcSwitch_1.ethg++ <--> Eth1G <--> centralSwitch_1.ethg++;
        qcSwitch_2.ethg++ <--> Eth1G <--> centralSwitch_1.ethg++;

        qcSwitch_1.ethg++ <--> Eth1G <--> centralSwitch_3.ethg++;
        qcSwitch_2.ethg++ <--> Eth1G <--> centralSwitch_2.ethg++;

		// Cameras
        Camera_1.ethg++ <--> Eth100M <--> qcSwitch_1.ethg++;
        Camera_2.ethg++ <--> Eth100M <--> qcSwitch_1.ethg++;

        // Monitoring
        SCADA.ethg++ <--> Eth100M <--> qcSwitch_2.ethg++;
        HMI.ethg++ <--> Eth100M <--> qcSwitch_2.ethg++;

        // Edge (Multiple Edge Computing, e.g. Server Vision, Cloud gateway)
        centralSwitch_3.ethg++ <--> Eth100M <--> MEC.ethg++;
        
        // Clock Distr. Eth [0] for switches
        masterClock.ethg++ <--> Eth100M <--> centralSwitch_1.ethg++ if exists(masterClock);

}
