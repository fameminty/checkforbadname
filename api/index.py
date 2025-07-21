const BadNames = {
    // name : hours banned for
    // 0 hours = perm
    "_": 0, // cheating no name
    "NIG": 24, // obvious reasons
};

const AllowedNames = [
    "MINIGAMES" // contains NIG so make it a allowed name
];

handlers.CheckForBadName = function(args, context) {
    const Name = args.name;
    const ForRoom = args.forRoom; // is for room (false if for troop/name)

    for (let badName in BadNames) {
        if (Name.includes(badName) && !AllowedNames.includes(Name)) {
            if (BadNames[badName] == 0) {
                server.BanUsers({
                    Bans: [{
                        PlayFabId: currentPlayerId,
                        DurationInHours: BadNames[badName],
                        Reason: "RULE BREAKING NAME: " + Name.toUpperCase() + ". PERMANENT BAN. USE YOUR HEAD NEXT GAME YOU PLAY."
                    }]
                });

                return {
                    "result": 2,
                    "banLength": 0
                };
            }

            server.BanUsers({
                Bans: [{
                    PlayFabId: currentPlayerId,
                    DurationInHours: BadNames[badName],
                    Reason: "RULE BREAKING NAME: " + Name.toUpperCase() + ". " + BadNames[badName] + " HOUR BAN. USE YOUR HEAD NEXT TIME."
                }]
            });

            return {
                "result": 2,
                "banLength": BadNames[badName]
            };
        }
    }

    return {
        "result": 0,
        "banLength": -1
    };
};
