from flask import Flask
import numpy as np
import pandas as pd
ipl_matches = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRy2DUdUbaKx_Co9F0FSnIlyS-8kp4aKv_I0-qzNeghiZHAI_hw94gKG22XTxNJHMFnFVKsO4xWOdIs/pub?gid=1655759976&single=true&output=csv"
matches = pd.read_csv(ipl_matches)

matches.head(5)
def get_teams():
    all_teams = matches['Team'].unique() + matches['Against'].unique()

    teams_dict = {"teams":all_teams}
    return teams_dict

get_teams()

def get_matches(team1, team2):
    
    valid_teams = list(set(matches['Team'].unique() + matches['Against'].unique()))
    if team1 not in valid_teams or team2 not in valid_teams:
        return "Invalid team name"
        
    matches = pd.read_csv(ipl_matches)
    matched_matches = ((matches[matches['Team'] == team1]) & (matches[matches['Against'] == team2])) | ((matches[matches['Team'] == team2]) & (matches[matches['Against'] == team1]))
    total_matches = matched_matches.shape[0]

    won_by_team1 = matched_matches[matched_matches['WinningTeam'] == team1].shape[0]
    won_by_team2 = matched_matches[matched_matches['WinningTeam'] == team2].shape[0]
    
    draws = total_matches - (won_by_team1 + won_by_team2)
    matched_dict = {
        "Total matched": total_matches,
        "Won by team1": won_by_team1,
        "Won by team2": won_by_team2,
        "Draws": draws,
        }
    return matched_dict
print(get_matches('RCB', 'MI'))
